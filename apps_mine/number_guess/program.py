import random

lower_bound = int(input("Lower bound "))
upper_bound = int(input("Upper bound "))

answer = random.randint(lower_bound, upper_bound)

# game loop
while True:
    # cast input string to int
    try:
        guess = int(input("Guess num between {0} and {1} ".format(lower_bound, upper_bound)))
    except ValueError:
        print("What???")
        continue

    if guess < lower_bound or guess > upper_bound:
        print("guess is out of bounds")
    elif answer > guess:
        print("guess is too low")
    elif answer < guess:
        print("guess to too high")
    elif answer == guess:
        print("Winner!")
        again_response = input("Again? ").lower()
        if 'y' in again_response:
            lower_bound = int(input("Lower bound "))
            upper_bound = int(input("Upper bound "))

            answer = random.randint(lower_bound, upper_bound)
        else:
            print("see ya later!")
            break
    else:
        print("what???")
