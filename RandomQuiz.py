# Connie Ng
# 1/12/24
# Program a random quiz using true or false
import random

# A list of questions and their corresponding answers
questions = [
    {
        'question': "What was SETU(South East Technological University previously known as?",
        'options': ['Munster University', 'Waterford College', 'WIT(Waterford Institute of Technology)', 'UCC(University College Cork)'],
        'answer': 'WIT(Waterford Institute of Technology)'
    },
    {
        'question': "What year did WIT become SETU?",
        'options': ['1970', '2022', '1997', '2000'],
        'answer': '2022'
    },
    {
        'question': "Who is the president at SETU?",
        'options': ['Professor Maggie Cusack', 'Professor Veronica Campbell', 'Professor Orla Feely', 'John OHalloran'],
        'answer': 'Professor Veronica Campbell'
    },
    {
        'question': "How many campuses does SETU have??",
        'options': ['3', '5', '8', '6'],
        'answer': '5'
    },
    {
        'question': "Which ocean is the largest?",
        'options': ['Atlantic', 'Indian', 'Arctic', 'Pacific'],
        'answer': 'Pacific'
    }
]

# Function to ask questions and check answers
def ask_question(question_data):
    print(f"Question: {question_data['question']}")
    print("Options:")
    
    for index, option in enumerate(question_data['options']):
        print(f"{index + 1}. {option}")
    
    try:
        answer = int(input("Choose the correct option (1/2/3/4): "))
        if question_data['options'][answer - 1] == question_data['answer']:
            print("Correct!\n")
            return True
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}\n")
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number between 1 and 4.\n")
        return False

# Main function to run the quiz
def run_quiz():
    score = 0
    random.shuffle(questions)  # Shuffle the questions to make the quiz random each time
    for question_data in questions:
        if ask_question(question_data):
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")

# Start the game
if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    run_quiz()
