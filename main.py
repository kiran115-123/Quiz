Questions = [
    "How many players are there in traditional Ludo?",
    "What is the square root of 169?",
    "Who's known as the Iron Man of India?",
    "What is the chemical symbol for gold?",
    "Who developed the theory of relativity?"
    "Which planet is known as the Red Planet?"
    "Who wrote the play "Romeo and Juliet"?"
    "What is the largest ocean on Earth?"
    "What is the longest river in the world?"
]

Options = [
    ["1. 4", "2. 5", "3. 6", "4. 7"],
    ["1. 52", "2. 15", "3. 13", "4. 14"],
    ["1. Tony Stark", "2. Sardar Vallabhbhai Patel", "3. Mahatma Gandhi", "4. Narendra Modi"],
    ["1. Ag", "2. Au", "3. NaCl", "4. length x breadth"],
    ["1. Michael Faraday", "2. Charles Darwin", "3. Abdul Kalam", "4. Albert Einstein"]
    ["1. Earth", "2. Mars", "3. Venus", "4. Jupiter"]
    ["1. Charles Dickens", "2. Jane Austen", "3. William Shakespeare", "4. Leo Tolstoy"]
    ["1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"]
    ["1. Amazon River", "2. Nile River", "3. Mississippi River", "4. Yangtze River"]
]

Answers = [1, 3, 2, 2, 4, 2, 3, 4,2]  # Correct answers for each question (index corresponds to the question)

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
