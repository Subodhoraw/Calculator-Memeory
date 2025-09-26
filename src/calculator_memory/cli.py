import sys
from .calculator import Calculator

class CalculatorCLI:
    """Command Line Interface for the Calculator with Memory."""
    
    def __init__(self):
        self.calc = Calculator()
        self.running = True
    
    def display_help(self):
        """Display help information."""
        help_text = """
Calculator with Memory - Commands:
---------------------------------
Basic Operations:
  add <num1> <num2>      - Add two numbers
  sub <num1> <num2>      - Subtract two numbers
  mul <num1> <num2>      - Multiply two numbers
  div <num1> <num2>      - Divide two numbers
  pow <num1> <num2>      - Power operation (num1^num2)
  sqrt <num>             - Square root of a number

Memory Operations:
  store <num>            - Store number in memory
  recall                 - Recall number from memory
  clear_mem              - Clear memory
  add_mem <num>          - Add number to memory
  sub_mem <num>          - Subtract number from memory

Using Memory in Calculations:
  madd <num>             - Add number to memory value
  msub <num>             - Subtract number from memory value
  mmul <num>             - Multiply memory by number
  mdiv <num>             - Divide memory by number
  mpow <num>             - Memory raised to power of number
  msqrt                  - Square root of memory

Other Commands:
  history                - Show calculation history
  clear_history          - Clear history
  help                   - Show this help message
  exit                   - Exit the calculator
        """
        print(help_text)
    
    def parse_input(self, user_input):
        """Parse user input and return command and arguments."""
        parts = user_input.strip().split()
        if not parts:
            return None, []
        
        command = parts[0].lower()
        args = []
        
        for part in parts[1:]:
            try:
                # Handle negative numbers
                if part.startswith('-') and part[1:].replace('.', '').isdigit():
                    args.append(float(part))
                elif part.replace('.', '').isdigit():
                    args.append(float(part))
                else:
                    print(f"Warning: '{part}' is not a valid number")
                    return None, []
            except ValueError:
                print(f"Warning: '{part}' is not a valid number")
                return None, []
        
        return command, args
    
    def handle_command(self, command, args):
        """Handle calculator commands."""
        try:
            if command == 'add':
                if len(args) == 2:
                    result = self.calc.add(args[0], args[1])
                    print(f"Result: {result}")
                else:
                    print("Usage: add <num1> <num2>")
            
            elif command == 'sub':
                if len(args) == 2:
                    result = self.calc.subtract(args[0], args[1])
                    print(f"Result: {result}")
                else:
                    print("Usage: sub <num1> <num2>")
            
            elif command == 'mul':
                if len(args) == 2:
                    result = self.calc.multiply(args[0], args[1])
                    print(f"Result: {result}")
                else:
                    print("Usage: mul <num1> <num2>")
            
            elif command == 'div':
                if len(args) == 2:
                    result = self.calc.divide(args[0], args[1])
                    print(f"Result: {result}")
                else:
                    print("Usage: div <num1> <num2>")
            
            elif command == 'pow':
                if len(args) == 2:
                    result = self.calc.power(args[0], args[1])
                    print(f"Result: {result}")
                else:
                    print("Usage: pow <num1> <num2>")
            
            elif command == 'sqrt':
                if len(args) == 1:
                    result = self.calc.square_root(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: sqrt <num>")
            
            # Memory operations
            elif command == 'store':
                if len(args) == 1:
                    self.calc.store_memory(args[0])
                    print(f"Stored {args[0]} in memory")
                else:
                    print("Usage: store <num>")
            
            elif command == 'recall':
                memory_value = self.calc.recall_memory()
                print(f"Memory: {memory_value}")
            
            elif command == 'clear_mem':
                self.calc.clear_memory()
                print("Memory cleared")
            
            elif command == 'add_mem':
                if len(args) == 1:
                    self.calc.add_to_memory(args[0])
                    print(f"Added {args[0]} to memory")
                else:
                    print("Usage: add_mem <num>")
            
            elif command == 'sub_mem':
                if len(args) == 1:
                    self.calc.subtract_from_memory(args[0])
                    print(f"Subtracted {args[0]} from memory")
                else:
                    print("Usage: sub_mem <num>")
            
            # Memory-based calculations
            elif command == 'madd':
                if len(args) == 1:
                    result = self.calc.add(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: madd <num>")
            
            elif command == 'msub':
                if len(args) == 1:
                    result = self.calc.subtract(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: msub <num>")
            
            elif command == 'mmul':
                if len(args) == 1:
                    result = self.calc.multiply(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: mmul <num>")
            
            elif command == 'mdiv':
                if len(args) == 1:
                    result = self.calc.divide(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: mdiv <num>")
            
            elif command == 'mpow':
                if len(args) == 1:
                    result = self.calc.power(args[0])
                    print(f"Result: {result}")
                else:
                    print("Usage: mpow <num>")
            
            elif command == 'msqrt':
                result = self.calc.square_root()
                print(f"Result: {result}")
            
            # History commands
            elif command == 'history':
                history = self.calc.get_history()
                if history:
                    print("Calculation History:")
                    for i, entry in enumerate(history, 1):
                        print(f"{i}. {entry}")
                else:
                    print("History is empty")
            
            elif command == 'clear_history':
                self.calc.clear_history()
                print("History cleared")
            
            elif command == 'help':
                self.display_help()
            
            elif command == 'exit':
                self.running = False
                print("Goodbye!")
            
            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
    
    def run(self):
        """Main loop for the CLI interface."""
        print("Welcome to Calculator with Memory!")
        print("Type 'help' for available commands or 'exit' to quit.")
        
        while self.running:
            try:
                user_input = input("\ncalc> ")
                command, args = self.parse_input(user_input)
                
                if command is None and user_input.strip():
                    continue  # Invalid input, try again
                
                if command:
                    self.handle_command(command, args)
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except EOFError:
                print("\n\nGoodbye!")
                break

def main():
    """Entry point for the CLI application."""
    cli = CalculatorCLI()
    cli.run()

if __name__ == "__main__":
    main()