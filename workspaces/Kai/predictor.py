
import os
import pickle
import numpy as np
import json

labels = ["False", "True"]

# life relocation model
class PythonPredictor:
    def __init__(self, config):
        """
        if os.environ.get("AWS_ACCESS_KEY_ID"):
            s3 = boto3.client("s3")  # client will use your credentials if available
        else:
            s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))  # anonymous client

        s3.download_file(config["bucket"], config["key"], "/tmp/model.pkl")
        """
        self.model = pickle.load(open("life_allocation.pkl", "rb"))

    def predict(self, payload):
   
        proba = self.model.predict_proba(payload['data']).tolist()
        label = self.model.predict(payload['data']).tolist()
        return json.dumps({'prob':proba, 'label':label})
