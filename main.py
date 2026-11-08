import random

print("Welcome to the Microbiology Quiz!\n")
print("Quiz starting soon...")

questions = [
    {
        "question": "What is the study of fungi called?",
        "options": ["A. Virology", "B. Mycology", "C. Bacteriology", "D. Parasitology"],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a Gram-positive bacterium?",
        "options": ["A. Staphylococcus aureus", "B. Streptococcus pyogenes", "C. Escherichia coli", "D. Bacillus subtilis"],
        "answer": "C"
    },
    {
        "question": "Which fungus commonly affects the scalp (causing tinea capitis)?",
        "options": ["A. Candida albicans", "B. Trichophyton tonsurans", "C. Aspergillus niger", "D. Cryptococcus neoformans"],
        "answer": "B"
    },
    {
        "question": "Staphylococcus aureus is best described as:",
        "options": ["A. Gram-negative rod", "B. Gram-positive coccus in clusters", "C. Gram-positive rod", "D. Gram-negative coccus"],
        "answer": "B"
    },
    {
        "question": "Which enzyme is used in PCR because it can withstand high temperatures?",
        "options": ["A. DNA polymerase from E. coli", "B. Taq polymerase", "C. RNA polymerase", "D. Ligase"],
        "answer": "B"
    },
    {
        "question": "Nosocomial infections are infections that are:",
        "options": ["A. Acquired in the community", "B. Acquired in a hospital or healthcare setting", "C. Caused only by viruses", "D. Always fungal"],
        "answer": "B"
    },
    {
        "question": "What is the protein coat that surrounds the genetic material of a virus called?",
        "options": ["A. Capsule", "B. Capsid", "C. Envelope", "D. Cell wall"],
        "answer": "B"
    },
    {
        "question": "Which agar is commonly used to grow fungi?",
        "options": ["A. MacConkey agar", "B. Blood agar", "C. Sabouraud dextrose agar", "D. Mannitol salt agar"],
        "answer": "C"
    },
    {
        "question": "In the microbiology lab, the catalase test is used to differentiate:",
        "options": ["A. Gram-positive cocci", "B. Staphylococcus from Streptococcus", "C. Fungi from bacteria", "D. Viruses from bacteria"],
        "answer": "B"
    },
    {
        "question": "Which structure is found in all viruses?",
        "options": ["A. Cell wall", "B. Ribosomes", "C. Nucleic acid and capsid", "D. Mitochondria"],
        "answer": "C"
    }
]

random.shuffle(questions)

score = 0
print("Welcome to the Microbiology Quiz!\n")

for q in questions:
    print("-------------------")
    print(q["question"])
    for option in q["options"]:
        print(option)

    while True:
        try:
            guess = input("Enter (A, B, C, D):").upper()
            if guess not in ["A", "B", "C", "D"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter A, B, C or D.")

    if guess == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q["answer"]}")


