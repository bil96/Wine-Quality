from src.WineQuality.config.configuration import ConfigurationManager
from src.WineQuality.components.data_transformation import DataTransformation
from src.WineQuality import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
      try:
            with open(Path("artifacts/data_validation/status.txt", "r")) as file:
                status = file.read().split(" ")[-1]
                if status == True:
                    config = ConfigurationManager()
                    data_transformation_config=config.get_data_transformation_config()
                    data_transformation = DataTransformation(config=data_transformation_config)
                    data_transformation.train_test_split()
                else:
                    raise Exception("Data Validation failed")

      except Exception as e:
          print(e)
