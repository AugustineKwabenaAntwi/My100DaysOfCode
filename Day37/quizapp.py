quiz = {
    "Question 1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "Question 2": {
        "question": "Which continent is known as the 'Land of the Rising Sun'?",
        "answer": "Asia"
    },
    "Question 3": {
        "question": "What is the longest river in the world?",
        "answer": "Nile"
    },
    "Question 4": {
        "question": "Which country is known as the 'Land of the Midnight Sun'?",
        "answer": "Norway"
    },
    "Question 5": {
        "question": "What is the largest ocean on Earth?",
        "answer": "Pacific Ocean"
    },
    "Question 6": {
        "question": "What is the tallest mountain in the world?",
        "answer": "Mount Everest"
    }
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if value['answer'].lower()==answer.lower():
        print(f'Correct')
        score=score + 1
    else:
        print(f"Wrong!!\n Correct Answer: {value['answer']}")

print(f"Your score: {score}")