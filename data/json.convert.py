import json

old_file = "questions.json"
new_file = "electrical.json"

with open(old_file, "r", encoding="utf-8") as f:
    questions = json.load(f)


new_structure = {
    "id": "electrical_safety",
    "title": "Электробезопасность",
    "description": "Проверка знаний по электробезопасности",
    "version": "1.0",
    "questions": questions
}


with open(new_file, "w", encoding="utf-8") as f:
    json.dump(
        new_structure,
        f,
        ensure_ascii=False,
        indent=4
    )

print("Готово")