class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
#2.define the functions    
    def add(self, num1, num2= None):
        if num2 is None:
            num2 = self.memory
            result = num1 + num2 
            self.history.append(f"Memory + {num1} = {result}")
        else:
            result = num1 + num2  
            self.history.append(f"{num1} +{num2} = {result}")
        return result
    def subtract(self, num1,num2 = None):
        if num2 is None:
            num2 = self.memory
            result = num1 - num2
            self.history.append(f"Memory - {num1} = {result}")
        else:
            result = num1 - num2
            self.history.append(f"{num1} - {num2} = {result}")
        return result
    def multiply(self, num1,num2 = None):
        if num2 is None:
            num2 = self.memory
            result = num1 * num2
            self.history.append(f"Memory * {num1} = {result}")
        else:
            result = num1 * num2
            self.history.append(f"{num1} * {num2} = {result}")
        return result
    def divide(self, num1,num2 = None):
        if num2 is None:
            num2 = self.memory
            if num2 == 0:
                return "Error! division by zero."
            result = num1 / num2
            self.history.append(f"Memory / {num1} = {result}")
        else:
            result = num1 / num2
            self.history.append(f"{num1} / {num2} = {result}")
        return result
    def avg(self, num1,num2 = None):
        if num2 is None:
            num2 = self.memory
            result = (num1 + num2) / 2
            self.history.append(f"Average of Memory and {num1} = {result}")
        else:
            result = (num1 + num2) / 2
            self.history.append(f"Average of {num1} and {num2} = {result}")
        return result
    def square_root(self, num):
        if num is None:
               if self.memory < 0:
                   return "Error! square root of negative number."
               result = num ** 0.5
               self.history.append(f"Square root of {num} = {result}")
        else:
            num ** 0.5
            self.history.append(f"Square root of {num} = {result}")
        return result
    