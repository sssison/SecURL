import pandas as pd                     # For data transformation
import numpy as numpy                   # For scientific calculations
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, classification_report
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, ConfusionMatrixDisplay
from xgboost import XGBClassifier, DMatrix, train
from sklearn.pipeline import Pipeline
import time
from datetime import datetime
import joblib
import os
import optuna
from sklearn.metrics import mean_squared_error # or any other metric
from sklearn.model_selection import train_test_split


def hyperparameter_tuning(X_train, y_train):
    """
    The function `hyperparameter_tuning` uses Optuna to optimize hyperparameters for an XGBoost model
    with early stopping based on the validation error.
    
    :param X_train: It seems like the description of the X_train parameter is missing. Could you please
    provide more information about the X_train parameter?
    :param y_train: It seems like the description of the 'y_train' parameter is missing. Could you
    please provide more information about the 'y_train' parameter so that I can assist you further with
    the hyperparameter tuning function?
    :return: The function `hyperparameter_tuning` returns the best hyperparameters found by the Optuna
    optimization process.
    """

    # Define the objective function for Optuna
    def objective(trial):
        # Define the search space for hyperparameters
        param = {
            'objective': 'binary:hinge',
            'eval_metric': 'error',
            'eta': trial.suggest_float('eta', 0.01, 0.3),
            'n_estimators': 100000, # Fix the boosting round and use early stopping
            'max_depth': trial.suggest_int('max_depth', 3, 10),
            'subsample': trial.suggest_float('subsample', 0.5, 1.0),
            'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
            'gamma': trial.suggest_float('gamma', 0.0, 10.0),
            'min_child_weight': trial.suggest_float('min_child_weight', 0.1, 10.0),
            'lambda': trial.suggest_float('lambda', 0.1, 10.0),
            'alpha': trial.suggest_float('alpha', 0.0, 10.0),
        }
        
        # Split the data into further training and validation sets (three sets are preferable)
        train_data, valid_data, train_target, valid_target = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
        
        # Convert the data into DMatrix format
        dtrain = DMatrix(train_data, label=train_target)
        dvalid = DMatrix(valid_data, label=valid_target)
        
        # Define the pruning callback for early stopping
        pruning_callback = optuna.integration.XGBoostPruningCallback(trial, 'validation-error')
        
        # Train the model with early stopping
        model = train(param, dtrain, num_boost_round=100000, evals=[(dvalid, 'validation')], early_stopping_rounds=100, callbacks=[pruning_callback])
        
        # Make predictions on the test set
        dtest = DMatrix(valid_data)
        y_pred = model.predict(dtest)
        
        # Calculate the root mean squared error
        error = mean_squared_error(valid_target, y_pred, squared=False)
        
        return error

    # Create an Optuna study and optimize the objective function
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=100) # Control the number of trials

    # Print the best hyperparameters and the best RMSE
    best_params = study.best_params

    return best_params

def model_training(X_train, y_train, X_test, y_test, best_params):
    """
    The function `model_training` trains an XGBoost classifier with specified parameters, evaluates its
    performance, and saves the trained model.
    
    :param X_train: X_train is the training data features, which are the input variables used to train
    the model. It typically consists of a matrix where each row represents a sample and each column
    represents a feature
    :param y_train: The `y_train` parameter in the `model_training` function represents the target
    labels for the training data `X_train`. It contains the true labels or classes that the model will
    learn to predict based on the input features in `X_train`
    :param X_test: X_test is the feature matrix representing the test data
    :param y_test: Y_test is the true labels of the test data, which will be used to evaluate the
    model's performance
    :param best_params: The `best_params` parameter is a dictionary containing the hyperparameters for
    the XGBoost model. It is used to specify the configuration of the XGBoost model during training
    """

    best_params['objective'] = 'binary:hinge'
    best_params['eval_metric'] = 'error'

    dtrain = DMatrix(X_train, label=y_train)
    dtest = DMatrix(X_test, label=y_test)

    xgb_classifier = train(best_params, dtrain, num_boost_round=5000)
    y_pred = xgb_classifier.predict(dtest)

    # Classification Report
    print(classification_report(y_test, y_pred))

    # Dumping the model
    joblib.dump(xgb_classifier, 'xgb_wrapper_25_lexical-content.sav')

def concept_drift_detector():
    