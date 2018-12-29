import math

class Calculator():
    def __init__(self, NumOne, NumTwo):
        self.NumOne = NumOne
        self.NumTwo = NumTwo
    
    def Addition(self):
        answer = self.NumOne + self.NumTwo
        return answer

    def Subtraction(self):
        answer = self.NumOne - self.NumTwo
        return answer
    
    def Multiplication(self):
        answer = self.NumOne * self.NumTwo
        return answer
    
    def Division(self):
        answer = self.NumOne / self.NumTwo
        return answer

p = input("Put in Num One: ")
pp = input("Put in Num Two: ")

a = Calculator(int(p), int(pp))

print("NumOne: ", a.NumOne, " NumTwo: ", a.NumTwo)
print("-------------------------------")
print("Added: ", a.Addition(), " Subtracted: ", a.Subtraction(), " Multiplied: ", a.Multiplication(), " Divided: ", a.Division())
    