from src.WineQuality.config.configuration import ConfigurationManager
from src.WineQuality.components.model_trainer import ModelTrainer
from src.WineQuality import logger

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            logger.exception(e)
            raise e