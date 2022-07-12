# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for answers in question_data:
    question_text = answers["text"]
    question_answer = answers["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
# q1 = question_data[0]["text"]
# a1 = question_data[0]["answer"]
# questions = Question(q1, a1)

quiz = Quizbrain(question_bank)
quiz.next_question()
quiz.still_has_questions()

# quiz.still_has_questions()

while quiz.still_has_questions():
    if quiz.next_question():
        quiz.next_question()



    # if quiz.answer == question_bank[quiz.question_number]["answer"]:
    #     print("Correct")
    # else:
    #     print("incorrect")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
