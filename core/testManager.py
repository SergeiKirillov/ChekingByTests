from pathlib import Path
import json
#from data.config.session import Session


class TestInfo():
    def __init__(self, file, idDB, title, description):
        self.file = file
        self.idDB = idDB
        self.title = title
        self.description = description


#[ ]: Нужло ли класс ТestManager вводить в  ApplicationContext

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

    def load_tests(self):
        tests = []
        #[ ]: TestManager - Возможно нужно использовать self.context.database.loadtest
        for file in Path(self.tests_dir).glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)
            tests.append(
                TestInfo(
                    file.stem, #[x]: Из file убрать путь и оставить только имя файла
                    data["idDB"],
                    data["title"],
                    data["description"]
                )
            )
        return tests




