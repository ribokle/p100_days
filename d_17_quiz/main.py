from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    question_bank.append(Question(questions['question'], questions['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.stii_has_questions():
    quiz.next_question()

print("Congratulations! You have completed the quiz.")
print(f"Your final score was {quiz.score}")