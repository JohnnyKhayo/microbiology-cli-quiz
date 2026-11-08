import random
import json

with open("database.json", "r") as file:
    questions = json.load(file)

print("Welcome to the Microbiology Quiz!\n")
print("Quiz starting soon...")


random.shuffle(questions)

score = 0

for q in questions:
    print("-------------------")
    print(q["question"])
    for option in q["options"]:
        print(option)

    while True:
        guess = input("Enter (A, B, C, D) or Q to quit:").strip().upper()
        if guess == "Q":
            print("Quiz ended early.")
            exit()
        if guess in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid input. Please enter A, B, C, D or Q.")

    if guess == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q["answer"]}")

percentage = (score/len(questions))* 100
print("\n-----------------")
print(f"Your final score: {score}/{len(questions)} ({percentage:.0f}%)")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 50:
    print("Good!")
else:
    print("Try Again")
