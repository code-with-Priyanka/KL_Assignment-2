# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        res = self.num1+self.num2
        return res
    def sub(self):
        res = self.num1-self.num2
        return res
    def mul(self):
        res = self.num1*self.num2
        return res
    def div(self):
        if self.num2 == 0:
            return "Error: division by zero"
        res = self.num1/self.num2
        return res    
def calculation():
    # Ask the user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Ask the user for the operator
    operator = input("Enter an operator (+, -, *, /): ")
    
    # Ask the user for the second number
    num2 = float(input("Enter the second number: "))
    calculator = Calculator(num1,num2)  
    # Perform the calculation based on the operator
    if operator == "+":
        result = calculator.add()
    elif operator == "-":
        result = calculator.sub()
    elif operator == "*":
        result = calculator.mul()
    elif operator == "/":
        result = calculator.div()
    else:
        print("Invalid operator.")
        return
    
    # Print the result
    print(f"{num1} {operator} {num2} = {result}")
    
    # Ask the user if they want to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (Y/N): ")
    if another_calculation.upper() == "Y":
        calculation()
    else:
        print("Goodbye!")

# Call the calculator function to start the program
calculation()
