from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

'''
CHALLENGE: 
Write a for loop to iterate over the question_data.
Create a Question object from each entry in question_data.
Append each Question object to the question_bank.
'''

# print (question_data[0]['text'])    #OUTPUT: text
# print(len(question_data))           #OUTPUT: 12

question_bank = []                    # This contains a list of questions

for n in range (0, len(question_data)):
    # print(question_data[n]['text'])
    question_text = question_data[n]["text"]
    answers = question_data[n]["answer"]
    new_question = Question(question_text, answers)
    question_bank.append(new_question)
    print(question_text)
    print(answers)

print(question_bank)
print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
quiz.next_question()
