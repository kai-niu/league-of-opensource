
import os
import pickle

labels = ["False", "True"]


class PythonPredictor:
    def __init__(self, config):
        """
        if os.environ.get("AWS_ACCESS_KEY_ID"):
            s3 = boto3.client("s3")  # client will use your credentials if available
        else:
            s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))  # anonymous client

        s3.download_file(config["bucket"], config["key"], "/tmp/model.pkl")
        """
        self.model = pickle.load(open("home_purchase.pkl", "rb"))

    def predict(self, payload):
   
        label_id = self.model.predict([payload['data']])[0]
        return labels[label_id]
