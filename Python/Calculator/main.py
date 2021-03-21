# put your python code here
def calculate(first_number, second_number, operation):
    if second_number == 0 and operation in ["/", "mod", "div"]:
        return "Division by 0!"
    else:
        if operation == "+":
            return first_number + second_number
        elif operation == "-":
            return first_number - second_number
        elif operation == "/":
            return first_number / second_number
        elif operation == "*":
            return first_number * second_number
        elif operation == "mod":
            return first_number % second_number
        elif operation == "pow":
            return first_number ** second_number
        elif operation == "div":
            return first_number // second_number
        else:
            return "Invalid operation!"


a = float(input())
b = float(input())
c = input()
print(calculate(a, b, c))
