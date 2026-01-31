import json
import random

def load_questions():
    with open("questions.json", "r") as file:
        return json.load(file)

def start_quiz():
    questions = load_questions()

    # Pick only 5 random questions
    if len(questions) > 5:
        questions = random.sample(questions, 5)

    score = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {q['question']}")

        for i, option in enumerate(q["options"], start=1):
            print(f"{i}. {option}")

        try:
            choice = int(input("Choose option (1-4): "))
            selected = q["options"][choice - 1]

            if selected == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
                print(f"Correct answer: {q['answer']}")

        except (ValueError, IndexError):
            print("Invalid input!")
            print(f"Correct answer: {q['answer']}")

    return score, len(questions)
