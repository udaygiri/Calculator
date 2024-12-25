import math 

class AdvancedOperations:

    @staticmethod
    def SquareRoot(expression):
        try:
            return str(math.sqrt(float(expression)))
        except:
            return "Error"
        

    @staticmethod
    def PercentageOfNumber(expression):
        try:
            return str(float(expression) / 100)
        except:
            return "Error"