'''
CHALLENGE:
Create a class called QuizBrain
Write an __init__() method
Initialise the question_number to 0
Initialise the question_list to an input
'''


class QuizBrain:

    def __init__(self, question_list):
        self.q_number = 0
        self.q_list = question_list

    '''
    #CHALLENGE:
    Retrieve the item from the current question_number from the question_list.
    Use the input() function to show the user the Question text and ask for the user's answer.
    '''

    def next_question(self):
        current_question = self.q_list[self.q_number]
        input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
