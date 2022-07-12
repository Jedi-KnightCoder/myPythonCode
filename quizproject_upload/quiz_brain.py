class Quizbrain:
    import random
    from data import question_data

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
            # print("True")
        else:
            return False



    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False)")
        # if q_answer == True:
        #     print("true")
        # elif q_answer == False:
        #     print("false")
        # else:
        #     print("none of the above")

        from data import question_data
        print(question_data[self.question_number]["answer"])
        if q_answer == question_data[self.question_number]["answer"]:
            print("Correct")
            return True
        else:
            print("incorrect")
            return False



