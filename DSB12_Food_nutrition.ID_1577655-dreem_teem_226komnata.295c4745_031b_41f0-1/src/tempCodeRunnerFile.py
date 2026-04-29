import pandas as pd
import numpy as np
import pickle
import requests

class Forecast:
    def __init__(self, model_path='model_rating.pkl', features_path='model_features.pkl'):
        self.model = None
        self.feature_names = []
        self._load_model(model_path, features_path)

    def _load_model(self, model_path, features_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        with open(features_path, 'rb') as f:
            self.feature_names = pickle.load(f)

    def predict(self, ingredients_list):
        """
        Predicts the rating category based on a list of ingredients.
        Returns: String (Bad, So-so, Great)
        """
        input_vector = np.zeros(len(self.feature_names))
        
        for i, feature in enumerate(self.feature_names):
            for ing in ingredients_list:
                if ing.strip().lower() in feature.lower():
                    input_vector[i] = 1.0
        
        prediction = self.model.predict([input_vector])[0]
        
        if prediction == 0:
            return "a bad idea"
        elif prediction == 1:
            return "so-so"
        else:
            return "a great idea"

class Nutritionist:
    def __init__(self):
        self.api_key = "06vkTKOSWiximfcB7ifbbEel7as3fAOG63IZjER3"
        self.base_url = "https://api.nal.usda.gov/fdc/v1"
        
        self.daily_values = {
            "Protein": 50.0,
            "Total lipid (fat)": 78.0,
            "Fatty acids, total saturated": 20.0,
            "Cholesterol": 300.0,
            "Carbohydrate, by difference": 275.0,
            "Sodium, Na": 2300.0,
            "Fiber, total dietary": 28.0,
            "Sugars, added": 50.0,
            "Calcium, Ca": 1300.0,
            "Iron, Fe": 18.0,
            "Potassium, K": 4700.0,
            "Vitamin C, total ascorbic acid": 90.0,
            "Vitamin A, RAE": 900.0,
            "Vitamin D (D2 + D3)": 20.0,
            "Vitamin E (alpha-tocopherol)": 15.0,
            "Vitamin K (phylloquinone)": 120.0,
            "Thiamin": 1.2,
            "Riboflavin": 1.3,
            "Niacin": 16.0,
            "Vitamin B-6": 1.7,
            "Folate, total": 400.0,
            "Vitamin B-12": 2.4,
            "Phosphorus, P": 1250.0,
            "Iodine, I": 150.0,
            "Magnesium, Mg": 420.0,
            "Zinc, Zn": 11.0,
            "Selenium, Se": 55.0,
            "Copper, Cu": 0.9,
            "Manganese, Mn": 2.3
        }

    def get_nutrition_facts(self, ingredient):
        """
        Fetches nutrition facts for a single ingredient.
        """
        # Search for the food
        search_url = f"{self.base_url}/foods/search"
        params = {
            "api_key": self.api_key,
            "query": ingredient,
            "pageSize": 1,
            "dataType": ["Foundation", "Survey (FNDDS)", "Branded"]
        }
        
        try:
            r = requests.get(search_url, params=params, timeout=10)
            r.raise_for_status()
            data = r.json()
            
            if not data.get("foods"):
                return None
            
            food_item = data["foods"][0]
            description = food_item["description"]
            
            nutrients = food_item.get("foodNutrients", [])
            
            facts = {}
            for n in nutrients:
                name = n["nutrientName"]
                amount = n["value"]
                
                dv_pct = None
                matched_key = None
                
                if name in self.daily_values:
                    matched_key = name
                else:
                    for key in self.daily_values:
                        if key.lower() in name.lower() or name.lower() in key.lower():
                            if "saturated" in name.lower() and "saturated" not in key.lower():
                                continue
                            matched_key = key
                            break
                
                if matched_key:
                    dv = self.daily_values[matched_key]
                    if dv > 0:
                        dv_pct = round((amount / dv) * 100)
                        facts[name] = dv_pct
            
            return {"name": description, "facts": facts}

        except Exception as e:
            print(f"Error fetching data for {ingredient}: {e}")
            return None

class SimilarRecipes:
    def __init__(self, data_path='recipes_processed.csv'):
        self.df = None
        self._load_data(data_path)

    def _load_data(self, path):
        try:
            self.df = pd.read_csv(path)
            self.metadata = self.df[['title', 'rating', 'url']]
            self.features = (
                self.df
                .drop(columns=['title', 'rating', 'url', 'url_slug'], errors='ignore')
                .select_dtypes(include=[np.number])
                .fillna(0)
            )
            self.all_columns = list(self.features.columns)
        except FileNotFoundError:
            print(f"Warning: {path} not found.")

    def find_top_3(self, ingredients_list):
        if self.df is None:
            return []

        target_columns = []
        
        for user_ing in ingredients_list:
            clean_ing = user_ing.strip().lower()
            if clean_ing.endswith('s'): 
                clean_ing = clean_ing[:-1]
            
            for col in self.all_columns:
                clean_col = col.lower()
                if (clean_ing in clean_col) or (clean_col in clean_ing):
                    # Защита от "apple" внутри "pineapple"
                    if "pineapple" in clean_col and "apple" in clean_ing and "pineapple" not in clean_ing:
                        continue
                    target_columns.append(col)

        # Удаляем дубликаты
        target_columns = list(set(target_columns))

        if not target_columns:
            return []

        scores = self.features[target_columns].sum(axis=1)

        result = (
            self.metadata
            .assign(match_score=scores)
            .query("match_score > 0")
            .sort_values(
                by=["match_score", "rating"],
                ascending=[False, False]
            )
            .head(3)
        )

        return result.to_dict(orient="records")

if __name__ == "__main__":
    pass

# 1. model_rating.pkl        # Обученная модель
# 2. model_features.pkl      # Список признаков
# 3. recipes_processed.csv   # Обработанные рецепты с бинарными признаками