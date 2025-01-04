Questions = [
    "How many players are there in traditional Ludo?",
    "What is the square root of 169?",
    "Who's known as the Iron Man of India?",
    "What is the chemical symbol for gold?",
    "Who developed the theory of relativity?"
]

Options = [
    ["1. 4", "2. 5", "3. 6", "4. 7"],
    ["1. 52", "2. 15", "3. 13", "4. 14"],
    ["1. Tony Stark", "2. Sardar Vallabhbhai Patel", "3. Mahatma Gandhi", "4. Narendra Modi"],
    ["1. Ag", "2. Au", "3. NaCl", "4. length x breadth"],
    ["1. Michael Faraday", "2. Charles Darwin", "3. Abdul Kalam", "4. Albert Einstein"]
]

Answers = [1, 3, 2, 2, 4]  # Correct answers for each question (index corresponds to the question)

score = 0  # Start score at 0
print("Rules: \n 1. Each question carries 100 points. \n 2. Answer questions by choosing options. \n 3. If you answer incorrectly, the game will end. \n Let's begin \n")

# Loop through each question
for i in range(len(Questions)):
    print(f"Question {i + 1}: {Questions[i]}")
    print("Options:")
    for option in Options[i]:
        print(option)
    
    value = int(input("Enter option: "))
    
    if value != Answers[i]:
        print("Answer is incorrect. Game over.")
        break
    else:
        score += 100  # Increase score by 100 for each correct answer
        print(f"Answer is correct! You get {score} points.")
    
print(f"Your total score is: {score}")
