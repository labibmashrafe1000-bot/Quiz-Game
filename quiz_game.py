# Quiz Game CLI

questions = {
    "What is the capital of France?": "Paris",
    "Which planet is known as the Red Planet?": "Mars",
    "What is 5 + 7?": "12",
    "Who wrote Hamlet?": "Shakespeare",
    "What is the largest ocean?": "Pacific"
}

score = 0

for question, answer in questions.items():
    print("\n" + question)
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {answer}")

print(f"\nYour final score is {score} out of {len(questions)}")
