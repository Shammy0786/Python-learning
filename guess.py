n=18
number_of_guesses=1
print("you have only 6 chances" )
while(number_of_guesses<=6):
    guess_number=int(input("guess the number\n"))
    if guess_number>18:
        print("decrease the number\n")
    elif guess_number<18:
        print("increase the number\n")
    else:
        print("congrest you won the game\n")
        print(number_of_guesses,"no of guesses took\n")
        break
    print(6-number_of_guesses,"no of guesses left")
    number_of_guesses=number_of_guesses+1

if number_of_guesses>6:
    print("game over")


