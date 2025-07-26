# Create a simple quiz app that asks questions, checks answers and tracks score
# In this program we will use a dictionary to store questions and answers and also a list to track the score
# Creat a dictionary inside a list to store questions and answers
quiz_questions = [
    {
        "question": "What is the capital city of kenya?",
        "options": ["A) Nairobi", "B) Mombasa", "C) Kisumu", "D) Nakuru"],
        "answer": "A"
    },
    {
        "question": "Who is the current president of Kenya?",
        "options": ["A) Raila Odinga", "B) William Ruto", "C) Uhuru Kenyatta", "D) Kalonzo Musyoka"],
        "answer": "B"
    },
    {
        "question": "Is Kenya located in East Africa?",
        "options": ["A) Yes", "B) No", "C) Maybe", "D) Not sure"],
        "answer": "A"
    }
]
# We will also check what they have scored
score = 0
for q in quiz_questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Please enter your answer (A, B, C, or D): ").strip().upper()
    if user_answer == q["answer"]: 
        print("Amazing! You are Correct!\n")
        score += 1
        
    else:
        print(f"Sorry, the correct answer is {q["answer"]}.")
    print(f"Your current score is: {score}\n")
print(f"Quiz completed! Your final score is: {score}/{len(quiz_questions)}")

