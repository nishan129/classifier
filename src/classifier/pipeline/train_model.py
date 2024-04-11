from src.classifier.entity.config_entity import TrainingConfig
from src.classifier.components.training import Training
from src.classifier.exception import ModelException
from src.classifier.logger import logging
import sys
from src.classifier.config.configuration import ConfigurationManager

STAGE_NAME = 'Train Model'

if __name__ == '__main__':
    try:
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
    except Exception as e:
        raise ModelException(e,sys)