questions = ["1. Which animal is known as the 'Ship of the Desert'?",
             "2. What is the largest mammal in the world?",
             "3. What is the fastest land animal?",
             "4. Which bird is known for its beautiful tail feathers?",
             "5. What is the only mammal capable of true flight?",]

answers = ["Camel", "Blue Whale", "Cheetah", "Peacock", "Bat"]
amount = [1000, 2000, 3000, 4000, 5000]
endAmount = 0

for i in range(len(questions)):
    print(questions[i])
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == answers[i].lower():
        print("Correct!")
        endAmount += amount[i]
    else:
        print(f"Incorrect! The correct answer is: {answers[i]}")
        break

print(f"Your final amount is: {endAmount}")