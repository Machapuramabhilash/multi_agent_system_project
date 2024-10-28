import pandas as pd

class ResearchAgent:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.data = self.load_dataset()

    def load_dataset(self):
        return pd.read_csv(self.dataset_path)
