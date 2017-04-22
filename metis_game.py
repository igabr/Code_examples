from random import randint
import os 
def game():
    counter = 1
    secret_number = randint(0,100)
    guess = -1
    while secret_number!= guess and counter <= 10:
        guess = input("Please make you guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print()
            print("Please enter an integer!")
            print()
            os.system('python game.py')
        print()
        if guess != secret_number:
            if guess > secret_number:
                print("Your guess was too high")
                print()
                counter+=1
            else:
                print("Your guess was too low")
                print()
                counter +=1
        else:
            print("You guessed right! - You win!")
    if counter == 11:
        print("Sorry, you are out of guesses! Please play again!")

if __name__ == "__main__":
    game()
