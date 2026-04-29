import numpy as np
import pandas as pd

def my_R2_score(y_true, y_pred):
	y_true = np.asarray(y_true, dtype=float).ravel()
	y_pred = np.asarray(y_pred, dtype=float).ravel()	

	return 1 - (np.sum((y_true - y_pred)**2) / np.sum((y_true - y_true.mean())**2))

def my_MAE(y_true, y_pred):
	y_true = np.asarray(y_true, dtype=float).ravel()
	y_pred = np.asarray(y_pred, dtype=float).ravel()	
	
	return np.mean(np.abs(y_true - y_pred))

def RMSE(y_true, y_pred):
	y_true = np.asarray(y_true, dtype=float).ravel()
	y_pred = np.asarray(y_pred, dtype=float).ravel()
	# находим MSE
	return np.mean((y_true - y_pred)**2)**0.5

def get_metrics(y_test, y_pred_test, y_train, y_pred_train, model_name):
    test_mae = my_MAE(y_test, y_pred_test)
    test_rmse = RMSE(y_test, y_pred_test)
    test_r2_score = my_R2_score(y_test, y_pred_test)

    train_mae = my_MAE(y_train, y_pred_train)
    train_rmse = RMSE(y_train, y_pred_train)
    train_r2_score = my_R2_score(y_train, y_pred_train)
    print(model_name)
    print(f'train \n{5*"="}\nMAE: {train_mae} \nRMSE: {train_rmse} \nR2: {train_r2_score}\n')
    
    print(f'test \n{5*"="}\nMAE: {test_mae} \nRMSE: {test_rmse} \nR2: {test_r2_score}\n')

    rmse_res = pd.DataFrame({
        'model':[model_name],
        'train': [train_rmse],
        'test': [test_rmse]
    })
    mae_res = pd.DataFrame({
        'model':[model_name],
        'train': [train_mae],
        'test': [test_mae]
    })

    r2_res = pd.DataFrame({
        'model':[model_name],
        'train': [train_r2_score],
        'test': [test_r2_score]
    })

    return mae_res, rmse_res, r2_res

def my_pipeline(
    model,
    x_test, y_test,
    x_train, y_train, 
    model_name		
):
    model.fit(x_train, y_train)
    y_pred_train = model.predict(x_train)
    y_pred_test = model.predict(x_test)
	
    return get_metrics(y_test, y_pred_test, y_train, y_pred_train, model_name)
    