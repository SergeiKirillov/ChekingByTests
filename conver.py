import json
import re
from docx import Document

def is_answer(line):
    return re.match(r"^\d+\.\s*", line.strip()) is not None

def is_question(line):
    return re.match(r"^\d+\.", line.strip()) and "?" in line

doc = Document("answ.docx")

questions = []

current_question = None
answers = []
question_id = 1

for paragraph in doc.paragraphs:

    text = paragraph.text.strip()

    if not text:
        continue

    # Новый вопрос
    if is_question(text):

        # Сохраняем предыдущий вопрос
        if current_question:
            questions.append({
                "id": question_id,
                "topic": "",
                "question": current_question,
                "answers": answers,
                "comment": ""
            })
            question_id += 1

        current_question = re.sub(r"^\d+\.\s*", "", text)
        answers = []

    # Ответ
    elif is_answer(text):

        answer_text = re.sub(r"^\d+\.\s*", "", text)

        correct = any(
            run.bold
            for run in paragraph.runs
            if run.text.strip()
        )

        answers.append({
            "text": answer_text,
            "correct": correct
        })

# Последний вопрос
if current_question:
    questions.append({
        "id": question_id,
        "topic": "",
        "question": current_question,
        "answers": answers,
        "comment": ""
    })

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(
        questions,
        f,
        ensure_ascii=False,
        indent=2
    )

print(f"Сконвертировано вопросов: {len(questions)}")