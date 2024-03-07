class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You're Right!")

        else:
            print("You're wrong!")
        print(f'The correct answer was: {correct_answer}.')
        print(f"Your current score is: {self.score}/{self.question_number}")
        print('\n'*2)

    def next_question(self):
        q_obj = self.question_list[self.question_number]
        self.question_number += 1
        answer = ''
        while answer != 'True' and answer != "False":
            answer = input(f"q.{self.question_number}: {q_obj.text} (True or False)? ").capitalize()

            if answer != "True" and answer != "False":
                print("Your answer must be 'True or False'!")

        self.check_answer(answer, q_obj.answer)

