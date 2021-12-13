# Create a class to work with the user inputs and give the results
class QuizBrain:
    def __init__(self, q_list):
        self.number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        '''check if quiz still has questions remaining'''
        if self.number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        '''Retrieve the item at the current question_number from the question list'''
        current_question = self.question_list[self.number]
        self.number += 1
        # show the user the question text and ask for the user's answer
        user_answer = input(f"Q.{self.number}: {current_question.question} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        '''Check if the user's answer input is right or wrong'''
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.number}")
        print("\n")