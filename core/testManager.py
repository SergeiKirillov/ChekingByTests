from pathlib import Path
import json
#from data.config.session import Session

class TestManager:
    def __init__(self, context):
        self.context = context
        self.tests_dir = Path("data/tests")
    
    def get_tests(self):
        return sorted(self.tests_dir.glob("*.json"))
    
    def get_tests_names(self):
        return[f.stem for f in self.get_tests()]
    
    def load_test(self):
        filename = self.tests_dir / f"{self.context.session.theme}.json"
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)