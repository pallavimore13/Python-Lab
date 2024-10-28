
import random

def initialization(s, e):
    print("Welcome")
    entry_fees = 20
    print(f"Pay the {entry_fees} and start the game")
    rewards = {1: 5.0, 2: 3.0, 3: 2.0, 4: 1.5, 5: 1.0}
    
    sn = random.randint(s, e)
    return sn, entry_fees, rewards  # Return values for unpacking

def start_game(sn, entry_fees, rewards):
    for attempt in range(1, 6):
        print(f"Attempt: {attempt}")
        guess = int(input("Guess the number: "))
        if guess == sn:
            prize = entry_fees * rewards[attempt]
            print(f"Congratulations! You win {prize}!")
            return prize
        else:
            print("Sorry, try again.")
    return -1 * entry_fees  # Penalty if all attempts are used up

def stop_game(status):
    if status > 0:
        print("Congratulations! Your guess was correct!")
    else:
        print("Better luck next time.")

def guess_the_number_and_win_prize():
    sn, entry_fees, rewards = initialization(1, 20)
    prize = start_game(sn, entry_fees, rewards)
    print(f"The number was {sn}. Final prize: {prize}")
    stop_game(prize)

guess_the_number_and_win_prize()




































