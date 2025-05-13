import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.WineQuality.entity.config_entity import ModelEvaluationConfig
from src.WineQuality.utils.common import save_json
from pathlib import Path
import os



class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_metrics(self,actual, predicted ):
        r2 = r2_score(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        mse = mean_squared_error(actual, predicted)
        rmse = np.sqrt(mse)

        return r2, mae, mse, rmse

    def log_into_mlflow(self):
        os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/bil96/Wine-Quality.mlflow"
        os.environ['MLFLOW_TRACKING_USERNAME'] = "bil96"
        os.environ['MLFLOW_TRACKING_PASSWORD'] = "99cc54f8815271eb745f16c20e6b33fe22603ab9"
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predict = model.predict(X_test)
            (r2, mae, mse, rmse) = self.evaluate_metrics(y_test, predict)
            scores = {"r2_score": r2, "mean_absolute_error": mae, "mean_squared_error": mse, "root_mean_squared_error": rmse}
            save_json(path=Path( self.config.metrics_file_name), data=scores)
            mlflow.log_params(self.config.all_params_path)

            mlflow.log_metric("rmse",rmse)
            mlflow.log_metric("r2",r2)
            mlflow.log_metric("mae",mae)

            if tracking_uri == "file":
                mlflow.sklearn.log_model(model,"model" ,registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")



