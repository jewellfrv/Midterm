import pandas as pd
import os

class HistoryManager:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path

    def save_record(self, record: dict):
        df = pd.DataFrame([record])
        if not os.path.isfile(self.file_path):
            df.to_csv(self.file_path, mode='w', header=True, index=False)
        else:
            df.to_csv(self.file_path, mode='a', header=False, index=False)

    def load_history(self):
        if os.path.isfile(self.file_path):
            return pd.read_csv(self.file_path)
        return pd.DataFrame()

    def clear_history(self):
        pd.DataFrame().to_csv(self.file_path, index=False)
