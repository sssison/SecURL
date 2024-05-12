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

# For Concept Drift
from frouros.datasets.synthetic import SEA
from frouros.detectors.concept_drift import DDM, DDMConfig
from frouros.metrics.prequential_error import PrequentialError


def hyperparameter_tuning(X_train, y_train):
    """
    The function `hyperparameter_tuning` uses Optuna to optimize hyperparameters for an XGBoost model
    with early stopping based on binary hinge loss and error evaluation metric.
    
    :param X_train: It seems like the input for X_train is missing. If you provide me with the X_train
    data, I can assist you in running the hyperparameter tuning function for your XGBoost model. Just
    paste the X_train data here, and I'll help you with the next steps
    :param y_train: The function `hyperparameter_tuning` you provided is for tuning hyperparameters of
    an XGBoost model using Optuna. It defines an objective function that Optuna will optimize to find
    the best hyperparameters for the model
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

def model_training(X_train, y_train, X_test, y_test, best_params, filename):
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

    print("Retraining still ongoing...")
    xgb_classifier = train(best_params, dtrain, num_boost_round=5000)
    y_pred = xgb_classifier.predict(dtest)

    # Classification Report
    print(classification_report(y_test, y_pred))

    # Dumping the model
    joblib.dump(xgb_classifier, filename)

    return

def concept_drift_detector(warm_up_pred, warm_up_act, test_pred, test_act):
    """
    The function `concept_drift_detector` implements a drift detection algorithm using the DDM method
    with error metrics and a warm-up phase followed by a detection phase.
    
    :param warm_up: The `warm_up` parameter in the `concept_drift_detector` function represents the
    initial dataset used to train the drift detection model. This dataset is used to establish a
    baseline for the model before testing it on a separate dataset to detect any concept drift
    :param testing: The `testing` parameter in the `concept_drift_detector` function represents the
    dataset that you want to test for concept drift. This dataset is used in the detection phase to
    monitor the model's performance and detect any potential drift in the data distribution. The
    function iterates through the instances in the `
    :return: The function `concept_drift_detector` is returning an integer value based on the detection
    of drift in the input data. If drift is detected during the testing phase, the function returns 1.
    If no drift is detected, the function returns 0.
    """
    

    # Configuring the Detector
    config = DDMConfig(
        warning_level=2.0,
        drift_level=3.0,
        min_num_instances=len(
            warm_up_pred.index
        ),  # Minimum number of instances to start checking for drift
    )

    detector = DDM(
        config=config,
    )

    # Error Metrics
    metrics = [
        PrequentialError(
            alpha=alpha,
            name=f"alpha={alpha}",
        )
        for alpha in [1.0, 0.9999, 0.999]
    ]
    metrics_historic_detector = {f"{metric.name}": [] for metric in metrics}


    def error_scorer(y_true, y_pred):  # Error function
        return 1 - (y_true == y_pred)

    # Warm-Up Phase
    warm_up_predicted = warm_up_pred.iloc[:, 0].tolist()
    warm_up_actual = warm_up_act.iloc[:, 0].tolist()

    for y_pred, y_actual in zip(warm_up_predicted, warm_up_actual):
        error = error_scorer(y_true=y_actual, y_pred=y_pred)
        _ = detector.update(value=error)

        for metric_historic, metric in zip(metrics_historic_detector.keys(), metrics):
            metrics_historic_detector[metric_historic].append(metric(error))

    # Detection Phase
    idx_drift, idx_warning = [], []

    i = len(warm_up_pred.index)
    test_predicted = test_pred.iloc[:, 0].tolist()
    test_actual = test_act.iloc[:, 0].tolist()


    for y_pred, y_actual in zip(test_predicted, test_actual):

        error = error_scorer(y_true=y_actual, y_pred=y_pred)
        _ = detector.update(value=error)  # Detector's update

        # All the following lines are optional and only used for plotting the whole process
        for metric_historic, metric in zip(metrics_historic_detector.keys(), metrics):
            metrics_historic_detector[metric_historic].append(metric(error))

        status = detector.status
        if status["drift"]:
            # Drift detected
            print(f"Drift detected at index: {i}")
            idx_drift.append(i)
            detector.reset()  # Reset detector
            for metric in metrics:  # Reset metrics
                metric.reset()
            return 1  # Stop simulation
        elif status["warning"]:
            # Warning zone
            idx_warning.append(i)
        i += 1
    
    return 0