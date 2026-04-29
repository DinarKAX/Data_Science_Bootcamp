import argparse
from recipes import Forecast, Nutritionist, SimilarRecipes

def main():
    parser = argparse.ArgumentParser(description="Food and Nutrition Helper")
    parser.add_argument("ingredients", type=str, help="Comma separated list of ingredients (e.g., 'milk,honey,jam')")
    args = parser.parse_args()

    raw_input = args.ingredients
    ingredients = [x.strip() for x in raw_input.split(',')]

    forecaster = Forecast()
    nutritionist = Nutritionist()
    recommender = SimilarRecipes()

    # I. FORECAST
    print("I. OUR FORECAST")
    prediction = forecaster.predict(ingredients)
    
    if "great" in prediction:
        intro = "This sounds delicious!"
    elif "so-so" in prediction:
        intro = "It might be edible, but..."
    else:
        intro = "You might find it tasty, but in our opinion,"
        
    print(f"{intro} it is {prediction} to have a dish with that list of ingredients.")
    print("")

    # II. NUTRITION FACTS
    print("II. NUTRITION FACTS")
    for ing in ingredients:
        print(f"--- {ing.title()} ---")
        data = nutritionist.get_nutrition_facts(ing)
        
        if data:
            print(f"Source: {data['name']}")
            if not data['facts']:
                print("No major Daily Value nutrients found.")
            for nutrient, pct in data['facts'].items():
                print(f"{nutrient} - {pct}% of Daily Value")
        else:
            print("Could not retrieve data from USDA database (Check API key or spelling).")
        print("")

    # III. TOP-3 SIMILAR RECIPES
    print("III. TOP-3 SIMILAR RECIPES:")
    similar = recommender.find_top_3(ingredients)
    
    if similar:
        for item in similar:
            print(f"- {item['title']}, rating: {item['rating']}, URL:")
            print(f"  {item['url']}")
    else:
        print("No similar recipes found in the database.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")