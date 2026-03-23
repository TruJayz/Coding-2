# In your unit 3 folder, create a new document called activityMar19.py Copy and paste the questions into your document and then
#  answer the following questions. You are permitted to use your notes, w3schools, and work together to answer the questions.
# do your best to complete all questions. This activity is due at the end of class.


#  In your own words, what is the difference between a python class and a python object?
# Please write your resonse as a string data type. 

# 1. A python class is a blueprint for creating objects. A python object is an instance of a class. The class defines the


#  In your own words, what is a object property and and object method? Please
# write your response as a string data type.


# 2. An object property is a variable that is associated with an object. An object method is a function that is associated with an object. 

# 3. Create a unique python class. Your class should have 5 properties and 3 mtethods. 
# each method should do one of the following; 
# 1 method must do some type of operation with data; an arithmetic, logical, or comparison operation
# 1 method must take in a parameter and do some operation on the parameter
# 1 method must do some type of conditional (if/else) logic. 


class grade:
    def __init__(self, name, score, letter_grade, pass_fail, extra_credit):
        self.name = name
        self.score = score
        self.letter_grade = letter_grade
        self.pass_fail = pass_fail
        self.extra_credit = extra_credit

    def calculateletterGrade(self):
        if self.score >= 90:
            self.letter_grade = 'A'
        elif self.score >= 80:
            self.letter_grade = 'B'
        elif self.score >= 70:
            self.letter_grade = 'C'
        elif self.score >= 60:
            self.letter_grade = 'D'
        else:
            self.letter_grade = 'F'

    def extracredit(self, points):
        self.score += points
        self.calculateletterGrade()

    def checkpassfail(self):
        if self.score >= 60:
            self.pass_fail = 'Pass'
        else:
            self.pass_fail = 'Fail'