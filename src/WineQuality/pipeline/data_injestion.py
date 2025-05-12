from src.WineQuality.config.configuration import ConfigurationManager
from src.WineQuality.components.data_injestion import DataIngestion
from src.WineQuality import logger

STAGE_NAME="Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_injestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__=="__main__":
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
            obj=DataIngestionTrainingPipeline()
            obj.initiate_data_injestion
            logger.info(f">>>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<")
        except Exception as e:
            logger.exception(e)
            raise e
