import pandas as pd

class DataUnderstandingAgent:
    def load_and_clean(self, file_path):
        df = pd.read_csv(file_path)
        df = df.dropna()
        return df
