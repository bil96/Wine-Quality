from src.WineQuality import logger
from src.WineQuality.pipeline.data_injestion import DataIngestionTrainingPipeline
from src.WineQuality.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.WineQuality.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.WineQuality.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.WineQuality.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline
logger.info("Logging has been set up successfully.")


STAGE_NAME = "Data Ingestion stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_injestion()
        logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.initiate_data_validation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<)<<<<")
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.initiate_data_transformation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion =ModelTrainerTrainingPipeline()
   data_ingestion.initiate_model_trainer()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = ModelEvaluationTrainingPipeline()
   data_ingestion.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
     raise e

