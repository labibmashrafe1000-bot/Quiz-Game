# Quiz Game CLI

def run_quiz():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "Who wrote Hamlet?", "answer": "Shakespeare"},
        {"question": "What is the largest ocean?", "answer": "Pacific"}
    ]

    score = 0

    print("Welcome to the Quiz Game! Answer the questions below:\n")

    for idx, q in enumerate(questions, 1):
        while True:
            user_answer = input(f"{idx}. {q['question']}\nYour answer: ").strip()
            if user_answer:
                break
            print("Please enter an answer.")

        if user_answer.lower() == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['answer']}\n")

    print(f"Quiz complete! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_quiz()
