class Question_Manager:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def run_test(answers):
        score = 0
        for i in answers:
            user_answer = input(i.question)
            if user_answer == i.answer:
                score += 1
        return "You got " + str(score) + '/' + str(len(answers)) + " correct."