from src.classifier.entity.config_entity import TrainingConfig
from src.classifier.components.training import Training
from src.classifier.components.data_ingenstion import DataIngestion
from src.classifier.components.base_model import PrepareBaseModel
from src.classifier.exception import ModelException
from src.classifier.logger import logging
import sys
from src.classifier.config.configuration import ConfigurationManager
from src.classifier.pipeline.model_evaluation import EvaluationPipeline
from src.classifier.pipeline.prediction import PredictionPipeline

# STAGE_NAME = 'data_ingenstion'

# if __name__ == '__main__':
#     try:
#         config = ConfigurationManager()
#         data_ingenstion_config = config.get_data_ingestion_config()
#         data_ingenstion = DataIngestion(config=data_ingenstion_config)
#         data_ingenstion.download_file()
#         data_ingenstion.extract_zip_file()
#     except Exception as e:
#         raise ModelException(e,sys)
    
   
# STAGE_NAME = 'Base Model'

# if __name__ == '__main__':
#     try:
#         config = ConfigurationManager()
#         prepare_base_model_config = config.get_prepare_base_model_config()
#         prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
#         prepare_base_model.get_base_model()
#         prepare_base_model.update_base_model()
#     except Exception as e:
#         raise ModelException(e,sys)
    
     
    

# STAGE_NAME = 'Train Model'

# if __name__ == '__main__':
#     try:
#         config = ConfigurationManager()
#         training_config = config.get_training_config()
#         training = Training(config=training_config)
#         training.get_base_model()
#         training.train_valid_generator()
#         training.train()
#     except Exception as e:
#         raise ModelException(e,sys)
    

# STAGE_NAME = "Evaluation stage"

# if __name__ == '__main__':
#     try:
#         logging.info(f"*******************")
#         logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = EvaluationPipeline()
#         obj.main()
#         logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logging.exception(e)
#         raise e
    
    
predict = PredictionPipeline(filename="D:/Machine Learning project/classifier/classifier/artifacts/data_ingenstion/kidney-ct-scan-image/Tumor/Tumor- (76).jpg")
print(predict.predict())
