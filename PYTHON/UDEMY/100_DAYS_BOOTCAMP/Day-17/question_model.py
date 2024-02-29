# CHALLENGE: Create a question with an __init()__ method with TWO attributes: text and answer attribute

class Question:

    def __init__(self, question, answer):
        self.q = question
        self.ans = answer

quest_1 = Question("2+3=5", "True")

print(quest_1.q)
print(quest_1.ans)

