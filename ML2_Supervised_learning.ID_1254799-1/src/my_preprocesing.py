import pandas as pd
import numpy as np

class My_StandartScaler():
    def __init__(self, columns= None):
        self.columns = columns
        self.index_cols = []
        self.dtype_ = None
        self.mean = None
        self.std = None

	# fit происходит при df = DataFrame|Series
    def fit(self, df):
        if isinstance(df, pd.Series):
            self.mean = np.mean( df.to_numpy(), axis=0 )
            self.std = np.std( df.to_numpy(), axis=0 )
            self.dtype_ = 'Series'
            
        elif isinstance(df, pd.DataFrame):
            self.dtype_ = 'DataFrame'
            # получаем индексы колонок
            index_colums_dict = {col:i for i, col in enumerate(df.columns)}
            if self.columns is None:
                self.columns = df.columns.copy()
                self.index_cols = [i  for i in range(len(df.columns))]
                
            else:
                # проверка на существование колонок
                self.columns = [c for c in self.columns  if c in df.columns]
                self.index_cols = [index_colums_dict[i]  for i in self.columns]
                
            self.mean = np.mean( df[self.columns].to_numpy(), axis=0 )
            self.std = np.std( df[self.columns].to_numpy(), axis=0 )
        else:
            raise ValueError("Не верные данные для обучения")
    
    def transform(self, df):
        if self.mean is None or self.std is None:
            raise ValueError("Scaler не обучен")
        # принимаем DataFrame и переводим его в np
        df = np.asarray(df, dtype=float)
        scaled = df.copy()
        if self.dtype_ == 'DataFrame':	
            scaled[:, self.index_cols] = (df[:, self.index_cols] - self.mean)/self.std
            
        elif self.dtype_ == 'Series':
            scaled = (df - self.mean)/self.std
        
        return scaled
        
        
    def fit_transform(self, df):
        
        self.fit(df)
        
        return self.transform(df)
    
    def inverse_transform(self, df_scaled):
        df = df_scaled.copy()
        if self.dtype_ == 'DataFrame':
            df[:, self.index_cols] = df_scaled[:, self.index_cols] * self.std + self.mean 
            
        elif self.dtype_ == 'Series':
            df = df_scaled * self.std + self.mean 
        
        return df

class My_MinMaxScaler():
    def __init__(self, columns= None):
        self.columns = columns
        self.index_cols = []
        self.dtype_ = None
        self.col_max = None
        self.col_min = None

	# fit происходит при df = DataFrame|Series
    def fit(self, df):
        if isinstance(df, pd.Series):
            self.col_min = df.min()
            self.col_max = df.max()
            self.dtype_ = 'Series'
            
        elif isinstance(df, pd.DataFrame):
            self.dtype_ = 'DataFrame'
            # получаем индексы колонок
            index_colums_dict = {col:i for i, col in enumerate(df.columns)}
            if self.columns is None:
                self.columns = df.columns.copy()
                self.index_cols = [i  for i in range(len(df.columns))]
                
            else:
                # проверка на существование колонок
                self.columns = [c for c in self.columns  if c in df.columns]
                self.index_cols = [index_colums_dict[i]  for i in self.columns]
                
            self.col_min = df[self.columns].min().to_numpy()
            self.col_max = df[self.columns].max().to_numpy()
        else:
            raise ValueError("Не верные данные для обучения")
    
    def transform(self, df):
        if self.col_min is None or self.col_max is None:
            raise ValueError("Scaler не обучен")
        # принимаем DataFrame и переводим его в np
        df = np.asarray(df, dtype=float)
        scaled = df.copy()
        if self.dtype_ == 'DataFrame':	
            scaled[:, self.index_cols] = (df[:, self.index_cols] - self.col_min)/(self.col_max - self.col_min)
            
        elif self.dtype_ == 'Series':
            scaled = (df - self.col_min)/(self.col_max - self.col_min)
        
        return scaled
        
        
    def fit_transform(self, df):
        
        self.fit(df)
        
        return self.transform(df)
    
    def inverse_transform(self, df_scaled):
        df = df_scaled.copy()
        if self.dtype_ == 'DataFrame':
            df[:, self.index_cols] = df_scaled[:, self.index_cols]*(self.col_max - self.col_min) + self.col_min 
            
        elif self.dtype_ == 'Series':
            df = df_scaled*(self.col_max - self.col_min) + self.col_min 
        
        return df
