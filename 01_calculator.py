def calculate(a, op ,b):
    if op == "+":
        c = a + b
    elif op == "-":
        c = a - b
    elif op == "*":
        c = a * b
    elif op == "/":
        c = a / b
    elif op == "**":
        c = a ** b
    elif op == "%":
        c = a % b
    else:
        return "Invalid operator"
    return c

def main():
    history = []
    ans = None
    while True:
        user = input("Do you want to perform a calculation?history/quit? (y/history/q): ")
        if user == "history":
                print(history[-5:]) 
                continue
        if user == "q" or user == "Q":
            break

        try:
            raw_a = input("Enter first number/can type ans: ")
            if raw_a == "ans":
                if ans is None:
                    print("No previous answer yet!")
                    continue
                a = ans
            else:
                a=float(raw_a)
                
            op = input("Enter operator (+, -, *, /, **, %): ")
            b = float(input("Enter second number: "))
            c = calculate(a, op ,b)
            history.append(f" {a} {op} {b} = {c}")
            print(f"Result of {a} {op} {b} = {c}")
            ans = c
            
             
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue

main()