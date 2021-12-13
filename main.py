from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank that contains question object instead of normal dictionary of questions.
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

print(question_bank[0].question)

# Create a quiz object through QuizBrain class
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")