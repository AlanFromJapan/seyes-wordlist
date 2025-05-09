from seyes_wordlist import generate_page
import sys
import random

PLACEHOLDER = "__"


def math_addition(max_number=100):
    a = random.randint(1, 100)
    b = min(max_number -a, random.randint(1, 100))
    c = a + b

    lbl = [a, b, c]
    #clear one
    lbl[random.randint(0, 2)] = PLACEHOLDER

    return f"{lbl[0]} + {lbl[1]} = {lbl[2]}"


def math_substraction(min_number=0, max_number=100):
    a = random.randint(2, max_number)
    #dirty way to avoid x - x = 0 ... not very challenging
    b = a
    while b == a:
        b = min(min_number + a, random.randint(1, max_number))
    c = a - b

    lbl = [a, b, c]
    #clear one
    lbl[random.randint(0, 2)] = PLACEHOLDER

    return f"{lbl[0]} - {lbl[1]} = {lbl[2]}"


def math_multiplication(max_number=10):
    a = random.randint(1, max_number)
    b = random.randint(1, max_number)
    c = a * b

    lbl = [a, b, c]
    #clear one
    lbl[random.randint(0, 2)] = PLACEHOLDER

    return f"{lbl[0]} × {lbl[1]} = {lbl[2]}"


def math_division(max_number=10):
    #avoid x / 1 = x ... not very challenging
    a = random.randint(2, max_number)
    #dirty way to avoid x / x = 1 ... not very challenging
    b = random.randint(2, max_number)

    #ok, copilot, nice ...
    c = a * b

    lbl = [c, a, b]
    #clear one
    lbl[random.randint(0, 2)] = PLACEHOLDER

    return f"{lbl[0]} / {lbl[1]} = {lbl[2]}"


"""Weights must sum to 100"""
def generate_equations(count=10, weight_addition=30, weight_substraction=30, weight_multiplication=20):
    equations = []
    for _ in range(count):
        #randomly choose an operation
        op = random.randint(0, 100)
        if op < weight_addition:
            equations.append(math_addition())
        elif op < weight_addition + weight_substraction:
            equations.append(math_substraction())
        elif op < weight_addition + weight_substraction + weight_multiplication:
            equations.append(math_multiplication())
        else:
            equations.append(math_division())

    return equations


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("""
Usage: python3 seys_maths.py output_file [repeat]
    Generates a page of maths exercises generated randomly file.
        """)
        exit(1)
    
    if len(sys.argv) >= 2:
        repeat = False
        if len(sys.argv) >= 3:
            repeat = str(sys.argv[2]).lower() == "repeat"

        output_file = sys.argv[1] 
        if not output_file.lower().endswith(".png"):
            output_file = output_file[:-4] + ".png"

        #generate 35 equations, with mostly addition and substraction (left 10% for division)
        lines = generate_equations(count=70, weight_addition=35, weight_substraction=35, weight_multiplication=20)

        generate_page(lines, sys.argv[1] , repeat, two_columns=True)