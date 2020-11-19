
import os
import pickle

<<<<<<< HEAD
labels = ["True", "False"]
=======
labels = ["setosa", "versicolor", "virginica"]
>>>>>>> f8c9eeb007a6243380737fb73d6f2979ccb5d99d


class PythonPredictor:
    def __init__(self, config):
        """
        if os.environ.get("AWS_ACCESS_KEY_ID"):
            s3 = boto3.client("s3")  # client will use your credentials if available
        else:
            s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))  # anonymous client

        s3.download_file(config["bucket"], config["key"], "/tmp/model.pkl")
        """
<<<<<<< HEAD
        self.model = pickle.load(open("lgbm_model.pkl", "rb"))

    def predict(self, payload):
   
        label_id = self.model.predict([payload['data']])[0]
=======
        self.model = pickle.load(open("toy_model.pkl", "rb"))

    def predict(self, payload):
        measurements = [
            payload["sepal_length"],
            payload["sepal_width"],
            payload["petal_length"],
            payload["petal_width"],
        ]

        label_id = self.model.predict([measurements])[0]
>>>>>>> f8c9eeb007a6243380737fb73d6f2979ccb5d99d
        return labels[label_id]
