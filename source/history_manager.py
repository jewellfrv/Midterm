# This module manages the calculation history for the calculator.
# It uses Pandas to store, load, save, clear, and delete history records.

import os
import pandas as pd

class HistoryManager:
    # A class to handle storing, loading, saving, and clearing calculation history using Pandas
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path
        # Initialize the HistoryManager with a file path for storing history

    def save_record(self, record: dict):
        # Save the current history to a CSV file
        df = pd.DataFrame([record])
        if not os.path.isfile(self.file_path):
            df.to_csv(self.file_path, mode='w', header=True, index=False)
        else:
            df.to_csv(self.file_path, mode='a', header=False, index=False)

    def load_history(self):
        # Load the history from a CSV file
        if os.path.isfile(self.file_path):
            return pd.read_csv(self.file_path)
        return pd.DataFrame()

    def clear_history(self):
        # Clear the current history
        pd.DataFrame().to_csv(self.file_path, index=False)
        