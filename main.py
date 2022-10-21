from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for sent in question_data:
     questions  = sent["question"]
     answer = sent["correct_answer"]
     new_question = Question(questions, answer)
     question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
     quiz.next_question()

print("you have completed the quiz")
print(f"your final score as {quiz.score}/{quiz.question_number}")