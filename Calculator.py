print("Welcome to calculator!")
print("Available math operators: +, -, *, /, ",
      "\tmod (reminder of division), ",
      "\tpow (exponentiation), ",
      "\tdiv (integer division).",
      "If you want to exit the calculator enter Exit.", sep="\n")
print()


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


while True:
    a = input("Please enter the first value: ")
    if a == "Exit":
        print("Goodbye!")
        break

    if is_number(a):
        a = float(a)
    else:
        print("Please enter the number.")
        continue

    b = input("Please enter the second value: ")
    if b == "Exit":
        print("Goodbye!")
        break

    if is_number(b):
        b = float(b)
    else:
        print("Please enter the number.")
        continue

    c = input("Please enter the operation you want to do: ")
    if c == "Exit":
        print("Goodbye!")
        break
    elif c == "+":
        if (a + b) % 1 == 0:
            print(int(a + b))
        else:
            print(a + b)
    elif c == "-":
        if (a - b) % 1 == 0:
            print(int(a - b))
        else:
            print(a - b)
    elif c == "*":
        if (a * b) % 1 == 0:
            print(int(a * b))
        else:
            print(a * b)
    elif c == "/":
        if b == 0:
            print("Division by zero!")
        else:
            if (a / b) % 1 == 0:
                print(int(a / b))
            else:
                print(a / b)
    elif c == "mod":
        if b == 0:
            print("Division by zero!")
        else:
            if (a % b) % 1 == 0:
                print(int(a % b))
            else:
                print(a % b)
    elif c == "pow":
        if (a ** b) % 1 == 0:
            print(int(a ** b))
        else:
            print(a ** b)
    elif c == "div":
        if b == 0:
            print("Division by zero!")
        else:
            if (a // b) % 1 == 0:
                print(int(a // b))
            else:
                print(a // b)
    else:
        print("Invalid operation")
