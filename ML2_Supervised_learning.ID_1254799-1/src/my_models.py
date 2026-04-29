import numpy as np

class BaseClass():
	def __init__(self):
		self.w = None
	

	def _add_bias(self, X):
		return np.c_[np.ones(X.shape[0]), X]

	@staticmethod
	def _mse(y, y_pred):
		return np.mean((y -y_pred)**2)
	def predict(self, X):
		if self.coef_ is None:
			raise RuntimeError("Model is not fitted")

		X = np.asarray(X, dtype=float)
		return X @ self.coef_ + self.intercept_
	
class LinearRegressionAnalytic(BaseClass):    
	def fit(self, X, y):
		X = np.asarray(X, dtype=float)
		y = np.asarray(y, dtype=float)
		# добавляем свободный член
		ones = np.ones((X.shape[0], 1))
		X = np.hstack((ones, X))
        
		w = np.linalg.pinv(X) @ y
		self.intercept_ = w[0]
		self.coef_ = w[1:]

class LinearRegressionGradient(BaseClass):
    def __init__(self, learning_rate=0.01, n_iter=1000, tol=1e-6):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.tol = tol

        self.coef_ = None
        self.intercept_ = None
        self.loss_history_ = []    

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).ravel()

        n_samples = X.shape[0]

        X_bias = self._add_bias(X)
        n_features = X_bias.shape[1]
        X_tr = X_bias.T
        w = np.zeros(n_features)

        for i in range(self.n_iter):
            # forward
            y_pred = np.dot(X_bias, w)
            error = y_pred - y

            # gradient
            grad = (2 / n_samples) * np.dot(X_tr, error)

            # update
            w_new = w - self.learning_rate * grad

            # loss AFTER update
            loss = self._mse(y, np.dot(X_bias, w_new))
            self.loss_history_.append(loss)

            # convergence check
            if i > 0 and abs(self.loss_history_[-1] - self.loss_history_[-2]) < self.tol:
                break

            w = w_new

        self.intercept_ = w[0]
        self.coef_ = w[1:]    

	
class LinearRegressionSGD(BaseClass):
    def __init__(self, B = 150, learning_rate=0.01, random_state = 21, n_epohs=100, tol=1e-6, deterministic = False):
        self.learning_rate = learning_rate
        self.n_epohs = n_epohs
        self.tol = tol
        self.B = B
        self.deterministic = deterministic
        self.random_state = random_state
        
        self.coef_ = None
        self.intercept_ = None
        self.loss_history_ = []        
        
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float).ravel()
        X_bias = self._add_bias(X)

        n_samples, n_features = X_bias.shape[0], X_bias.shape[1]         

        w = np.zeros(n_features)

        for epoch in range(self.n_epohs):
            if self.deterministic:
                indices = range(n_samples)
            else:
                rng = np.random.default_rng(self.random_state)
                indices = rng.permutation(n_samples)
                indices = np.random.permutation(n_samples)
                
            for i in range(0, len(indices), self.B):                
                cur_X = np.take(X_bias, indices[i: i+self.B], axis = 0)                
                cur_y = np.take(y, indices[i: i+self.B], axis = 0)
                
                y_pred = np.dot(cur_X, w)
                error = y_pred - cur_y
    
                grad = (2 / len(cur_y)) * np.dot(cur_X.T, error) # градиент
    
                w = w - self.learning_rate * grad
    
            # loss AFTER update
            loss = self._mse(y, np.dot(X_bias, w))
            self.loss_history_.append(loss)
    
            # convergence check
            if epoch > 0 and abs(self.loss_history_[-1] - self.loss_history_[-2]) < self.tol:
                break

        self.intercept_ = w[0]
        self.coef_ = w[1:]    