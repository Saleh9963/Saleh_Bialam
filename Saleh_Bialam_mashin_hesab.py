# -*- coding: utf-8 -*-
import math


class AdvancedCalculator:
    def __init__(self):
        self.history = []

    # ---------- Basic Operations ----------
    def add(self, a, b):
        result = a + b
        self.save("Add", a, b, result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.save("Subtract", a, b, result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.save("Multiply", a, b, result)
        return result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.save("Divide", a, b, result)
        return result

    def power(self, a, b):
        result = a ** b
        self.save("Power", a, b, result)
        return result

    # ---------- Advanced Operations ----------
    def absolute(self, x):
        result = abs(x)
        self.save("Absolute", x, None, result)
        return result

    def square_root(self, x):
        if x < 0:
            return "Error: Negative number"
        result = math.sqrt(x)
        self.save("Square Root", x, None, result)
        return result

    def factorial(self, x):
        if x < 0 or int(x) != x:
            return "Error: Invalid input for factorial"
        result = math.factorial(int(x))
        self.save("Factorial", x, None, result)
        return result

    def sine(self, x):
        result = math.sin(math.radians(x))
        self.save("Sine", x, None, result)
        return result

    def cosine(self, x):
        result = math.cos(math.radians(x))
        self.save("Cosine", x, None, result)
        return result

    def tangent(self, x):
        result = math.tan(math.radians(x))
        self.save("Tangent", x, None, result)
        return result

    # ---------- Utility ----------
    def save(self, operation, a, b, result):
        self.history.append({
            "operation": operation,
            "a": a,
            "b": b,
            "result": result
        })

    def show_history(self):
        if not self.history:
            print("History is empty.")
            return
        print("\n----- Calculation History -----")
        for i, item in enumerate(self.history, 1):
            print(f"{i}) {item['operation']} -> Result: {item['result']}")

# ---------- Menu ----------


def show_menu():
    print("""
========= ADVANCED CALCULATOR =========
1) Add
2) Subtract
3) Multiply
4) Divide
5) Power
6) Absolute
7) Square Root
8) Factorial
9) Sine
10) Cosine
11) Tangent
12) Show History
0) Exit
""")


# ---------- Main ----------
calc = AdvancedCalculator()

while True:
    show_menu()
    try:
        choice = int(input("Your choice: "))

        if choice == 0:
            print("Exit program")
            break

        elif choice in [1, 2, 3, 4, 5]:
            a = float(input("First number: "))
            b = float(input("Second number: "))

            if choice == 1:
                print("Result:", calc.add(a, b))
            elif choice == 2:
                print("Result:", calc.subtract(a, b))
            elif choice == 3:
                print("Result:", calc.multiply(a, b))
            elif choice == 4:
                print("Result:", calc.divide(a, b))
            elif choice == 5:
                print("Result:", calc.power(a, b))

        elif choice in [6, 7, 8, 9, 10, 11]:
            x = float(input("Number: "))

            if choice == 6:
                print("Result:", calc.absolute(x))
            elif choice == 7:
                print("Result:", calc.square_root(x))
            elif choice == 8:
                print("Result:", calc.factorial(x))
            elif choice == 9:
                print("Result:", calc.sine(x))
            elif choice == 10:
                print("Result:", calc.cosine(x))
            elif choice == 11:
                print("Result:", calc.tangent(x))

        elif choice == 12:
            calc.show_history()

        else:
            print("Invalid choice!")

    except ValueError:
        print("Invalid input!")
