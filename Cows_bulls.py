import random


def generate_num():
    return [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]


def get_user_num():

    guess_wrong = True
    while guess_wrong:
        user_num_int = input("Please enter your guess (must be four digits): ")
        user_num_list = []
        for digit in str(user_num_int):
            user_num_list.append(int(digit))
        if len(user_num_list) != 4:
            print("The length of you guess is invalid, try again")
        if len(user_num_list) == 4:
            guess_wrong = False

    return user_num_list


def check_number(rand_num, guess):
    cows = 0
    moves = 0
    while cows < 4:
        cows = 0
        bulls = 0

        if cows < 4:
            for i in range(len(guess)):
                if guess[i-1] == rand_num[i-1]:
                    cows += 1
                if guess[i-1] != rand_num[i-1]:
                    bulls += 1
            moves +=1
            print("Bulls - " + str(bulls))
            print("Cows - " + str(cows))

            if cows == 4:
                if moves == 1:
                    print("Congratulations, you've won the number was " + str(rand_num) + " it took you "
                          + str(moves) + " move")
                else:
                    print("Congratulations, you've won the number was " + str(rand_num) + " it took you "
                          + str(moves) + " moves")
                break
        guess = get_user_num()


play_again = 'yes'
print("Welcome to the cows and bulls game!!!!")
print("--------------------------------------")
print("Rules:")
print("-  You must only enter 4 digit numbers")
print("-  Cow - digit is in the correct place")
print("-  Bull - digit in incorrect place")
while play_again == 'yes':
    generated = generate_num()
    user = get_user_num()
    check_number(generated, user)
    play_again = input("Would you like to play again (yes/no): ")

if play_again != 'yes':
    print("Thanks for playing!!")

