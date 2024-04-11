from src.classifier.entity.config_entity import DataIngestionConfig
from src.classifier.components.data_ingenstion import DataIngenstion
from src.classifier.exception import ModelException
from src.classifier.logger import logging
import sys
from src.classifier.config.configuration import ConfigurationManager

STAGE_NAME = 'data_ingenstion'

if __name__ == '__main__':
    try:
        config = ConfigurationManager()
        data_ingenstion_config = config.get_data_ingenstion_config()
        data_ingenstion = DataIngenstion(config=data_ingenstion_config)
        data_ingenstion.download_file()
        data_ingenstion.extract_zip_file()
    except Exception as e:
        raise ModelException(e,sys)