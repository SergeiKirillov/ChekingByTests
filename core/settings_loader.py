import json
from pathlib import Path


class SettingsLoader:
    
    @staticmethod
    def load():
        file_path = Path("data")/"settings.json"
        with open(file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        return data

