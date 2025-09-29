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
    def square_root(self, num = None):
        if num is None:
               if self.memory < 0:
                   return "Error! square root of negative number."
               result = self.memory ** 0.5
               self.history.append(f"Square root of {num} = {result}")
        else:
            if num < 0:
               return "Error! square root of negative number."
            results = num ** 0.5
            self.history.append(f"Square root of {num} = {result}")
        return result
    def store_in_memory(self,value):
        """Store a value in memory."""
        self.memory = value
        self.history.append(f"Stored {value} in memory.")
    def recall_memory(self):
        """Recall the value from memory."""
        self.history.append(f"Recalled {self.memory} from memory.")
        return self.memory
    def clear_memory(self):
        """Clear the memory."""
        self.memory = 0
        self.history.append("Cleared memory.")  
    def add_to_memory(self,value):
        """Add a value to the memory."""
        self.memory += value
        self.history.append(f"Added {value} to memory. New memory: {self.memory}")
    def subtract_from_memory(self,value):
        """Subtract a value from the memory."""
        self.memory -= value
        self.history.append(f"subtracted{value} from memory= {self.memory}")
    def get_history(self):
        """Get the history of calculations."""
        return self.history
    def clear_history(self):
        """ Clear the calculation history."""
        self.history.clear()
    
    
    