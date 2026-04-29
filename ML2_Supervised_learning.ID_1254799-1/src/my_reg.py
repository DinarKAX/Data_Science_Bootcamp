import numpy as np
from my_models import BaseClass

class RidgeGD(BaseClass):
    def __init__(self, l = 1.0, learning_rate=0.005, n_epohs=1000, tol=1e-6):
        self.learning_rate = learning_rate
        self.n_epohs = n_epohs
        self.tol = tol
        self.l = l # регулизация 
        
        self.coef_ = None
        self.intercept_ = None
        self.loss_history_ = []        
        
    def _init_weights(self, X_bias, y):
        n_features = X_bias.shape[1]
        try:
            w_init = np.linalg.pinv(X_bias.T @ X_bias + self.l*np.eye(n_features)) @ X_bias.T @ y
        except:
            scale = 1.0 / np.sqrt(n_features)
            w_init = np.random.randn(n_features)*scale
        return w_init
    
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).ravel()
        X_bias = self._add_bias(X)

        n_samples = X_bias.shape[0]

        w = self._init_weights(X_bias, y)
        
        best_loss = np.inf
        best_w = w.copy()

        for epoch in range(self.n_epohs):
            lr = self.learning_rate
            y_pred = np.dot(X_bias, w) # предсказывнаие модели
            error = y_pred - y # ошибка
    
            grad = (2 /	 n_samples) * np.dot(X_bias.T, error) # находим градиент
            grad[1:] += 2 * self.l * w[1:] # добавляем ругулизацию к весам параметров
            
            grad_norm = np.linalg.norm(grad) # находим норму градиента, чтобы узнать размер шага
            if grad_norm > 100: # чтобы не перейти его уменьшаем learning_rate
                lr = lr / 10
                
            lr = lr / (1 + 0.005*epoch) # уменьшение шага для последних эпох
                
            w_new = w - lr* grad # изменение весов
            
            loss = np.mean((X_bias @ w - y)**2) + self.l * np.sum(w[1:]**2)
            self.loss_history_.append(loss)
            
            if loss < best_loss:
                best_loss = loss 
                best_w = w_new.copy()            
                
            # convergence check
            if epoch > 0 and abs(self.loss_history_[-1] - self.loss_history_[-2]) < self.tol:
                w = best_w
                break
            
            w = w_new
            
            if not np.isfinite(loss):
                print(f"Warning: Non-finite loss at iteration {epoch}, using best weights")
                w = best_w
                break
            
        if best_loss < np.inf:
            w = best_w

        self.intercept_ = w[0]
        self.coef_ = w[1:]    

class LassoGD(BaseClass):
    def __init__(self, l = 1.0, learning_rate=0.005, n_epohs=1000, tol=1e-6):
        self.learning_rate = learning_rate
        self.n_epohs = n_epohs
        self.tol = tol
        self.l = l # регулизация 
        
        self.coef_ = None
        self.intercept_ = None
        self.loss_history_ = []        
            
    
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).ravel()
        X_bias = self._add_bias(X)

        n_samples, n_features = X_bias.shape

        w = np.zeros(n_features)            

        for epoch in range(self.n_epohs):
            lr = self.learning_rate
            y_pred = np.dot(X_bias, w) # предсказывнаие модели
            error = y_pred - y # ошибка
    
            grad = (2 /	 n_samples) * np.dot(X_bias.T, error) # находим градиент
            grad[1:] += self.l * np.sign(w[1:]) # добавляем ругулизацию к весам параметров
            
            w = w - lr* grad # изменение весов
            
            loss = np.mean((X_bias @ w - y)**2) + self.l * np.sum(np.abs(w[1:]))
            self.loss_history_.append(loss)

            if epoch > 0 and abs(self.loss_history_[-1] - self.loss_history_[-2]) < self.tol:
                break
                        
        self.intercept_ = w[0]
        self.coef_ = w[1:]    
        print(self.loss_history_)

class ElasticNetGD(BaseClass):
    def __init__(self, l1 = 1.0, l2 = 1.0, learning_rate=0.01, n_epohs=1000, tol=1e-6):
        self.learning_rate = learning_rate
        self.n_epohs = n_epohs
        self.tol = tol
        self.l1 = l1 # регулизация 
        self.l2 = l2
        
        self.coef_ = None
        self.intercept_ = None
        self.loss_history_ = []        
            
    
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).ravel()
        X_bias = self._add_bias(X)

        n_samples, n_features = X_bias.shape

        w = np.zeros(n_features)            

        for epoch in range(self.n_epohs):

            y_pred = np.dot(X_bias, w) # предсказывнаие модели
            error = y_pred - y # ошибка
    
            grad = (2 /	 n_samples) * np.dot(X_bias.T, error) # находим градиент
            grad[1:] += self.l1 * np.sign(w[1:]) # добавляем ругулизацию к весам параметров
            grad[1:] += 2*self.l2 *w[1:]

            w = w - self.learning_rate* grad # изменение весов
            
            loss = (
                np.mean((X_bias @ w - y)**2)
                + self.l1 * np.sum(np.abs(w[1:])) 
                + self.l2 *np.sum(w[1:]**2) 
			)
            self.loss_history_.append(loss)

            if epoch > 0 and abs(self.loss_history_[-1] - self.loss_history_[-2]) < self.tol:
                break
                        
        self.intercept_ = w[0]
        self.coef_ = w[1:]    
        print(self.loss_history_)