from source.history_manager import HistoryManager
import os
import pandas as pd

def test_save_and_load():
    manager = HistoryManager('test_history.csv')
    manager.save_record({'operation': 'add', 'result': 5})
    history = manager.load_history()
    assert not history.empty
    os.remove('test_history.csv')
