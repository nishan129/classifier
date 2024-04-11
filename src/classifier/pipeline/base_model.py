from src.classifier.entity.config_entity import BaseModelConfig
from src.classifier.components.base_model import PrepareBaseModel
from src.classifier.exception import ModelException
from src.classifier.logger import logging
import sys
from src.classifier.config.configuration import ConfigurationManager

STAGE_NAME = 'Base Model'

if __name__ == '__main__':
    try:
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
    except Exception as e:
        raise ModelException(e,sys)