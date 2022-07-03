import os
import pandas as pd
import numpy as np
from mlflow.pyfunc import load_model

# Called when the service is loaded
def init():
    global model
    
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "diabetes_model_oh4ml")
#    model_path = Model.get_model_path(args.model_name)
    model = load_model(model_path)  


def run(mini_batch):
    print(f"run method start: {__file__}, run({mini_batch})")
    
    for input in mini_batch:
        input_np = np.loadtxt(input, delimiter=',',skiprows=1)
        predictions = model.predict(input_np)
        log_txt = 'Predictions:' + str(predictions)
        print (log_txt)

    return pd.DataFrame(predictions) # return a dataframe or a list