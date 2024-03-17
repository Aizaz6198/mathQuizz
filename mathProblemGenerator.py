import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 15
total_problems = 10


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)

    return expression, answer


start_time = time.time()
for i in range(total_problems):
    expression, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expression + " = ")
        try:
            guess = int(guess)  # Convert input to integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Restart the loop
        if guess == answer:
            print("Correct!")
            break
        else:
            print("Incorrect.")
end_time = time.time()

print("\nAll problems solved!")
print("Time taken to solve all problems: {:.2f} seconds".format(end_time - start_time))
