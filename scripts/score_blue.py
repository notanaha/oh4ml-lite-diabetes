import os, json
import logging
import numpy as np
from mlflow.pyfunc import load_model


def init():
    global model

    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "diabetes_model_oh4ml")
    model = load_model(model_path)  


def run(raw_data):
    logging.info("diabetes_model_oh4ml: request received")
    data = json.loads(raw_data)["data"]
    data = np.array(data)
    result = model.predict(data)
    logging.info("Request processed")
    return result.tolist()
