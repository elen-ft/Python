import json

def load_questions_from_json(file_path):
    with open(file_path, 'r') as file:
        questions_data = json.load(file)
    return questions_data

def save_user_result_to_json(user_name, score):
    user_result = {
        'user_name': user_name,
        'score': score
    }
    with open('user_results.json', 'w') as file:
        json.dump(user_result, file)

def take_quiz(questions_data):
    score = 0
    for question_num, question in enumerate(questions_data, start=1):
        print(f"Question {question_num}: {question['question']}")
        user_answer = input("Your answer: ")
        if user_answer.lower() == question['answer'].lower():
            score += 1
    return score

questions_file = 'quiz.json'
questions_data = load_questions_from_json(questions_file)

user_name = input("Enter your name: ")
user_score = take_quiz(questions_data)

print(f"Quiz completed! Your score: {user_score}")

save_user_result_to_json(user_name, user_score)
