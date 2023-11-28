while True:
    try:
        MainMenu = 'y'
        while MainMenu == 'y':
            # intro / main menu start
            print('****************MAIN MENU****************\n')
            MenuChoice = int(input('Pick an option from the menu\n1 - Play\n2 - Instructions\n3 - Quit\nChoice: '))
            # quit check and making sure menu code doesn't start
            if MenuChoice == 3:
                MainMenu = 'n'
            # make sure nothing went wrong when chosing 1 of the 2 options other then qutiing
            while MenuChoice == 1 or MenuChoice == 2:

                # checking to play instructions
                if MenuChoice == 2:
                    print(
                        'Welcome to Word Guesser!\n''In this game you will guess the letters of a secret word to\ntry and determine what it is.\n''Be carefull you only have 5 incorrect guesses')
                    # set back to main menu and stop looping choice
                    MainMenu = 'y'
                    MenuChoice = 0

                # checking if they wanted to start the game
                # will show the words so dont look until after you play
                if MenuChoice == 1:
                    # variables for words / lists
                    incorrectChoice = 0
                    # wordlist len values
                    WordList = ['cat', 'dog', 'eat', 'bat', 'fate']
                    # assign astrix ammount / auto reset the words
                    displayWord1 = ['*', '*', '*']
                    displayWord2 = ['*', '*', '*']
                    displayWord3 = ['*', '*', '*']
                    displayWord4 = ['*', '*', '*']
                    displayWord5 = ['*', '*', '*', '*']
                    print('\nThere are 5 words to choose from. Which word would you like\nto use?')
                    wordPicked = int(input('Please enter a number (1 - 5): '))

                    # code for all the words / guesses

                    # for 1st word
                    while wordPicked == 1:
                        print('Your word has', (len(WordList[0])), 'letters good luck!')
                        print(displayWord1)

                        LetterGuessed = str(input('Guess a letter: '))
                        # checking to see if they already guessed the letter
                        if LetterGuessed == 'c':
                            if displayWord1[0] == 'c':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'a':
                            if displayWord1[1] == 'a':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 't':
                            if displayWord1[2] == 't':
                                print('why are you guessing a letter you already guessed :|')

                        if LetterGuessed == 'c':
                            print(LetterGuessed, 'is in the word')
                            displayWord1[0] = 'c'

                        if LetterGuessed == 'a':
                            print(LetterGuessed, 'is in the word')
                            displayWord1[1] = 'a'

                        if LetterGuessed == 't':
                            print(LetterGuessed, 'is in the word')
                            displayWord1[2] = 't'

                        if LetterGuessed != 'c' and LetterGuessed != 'a' and LetterGuessed != 't':
                            print('incorrect choice sorry')
                            incorrectChoice = incorrectChoice + 1
                        if displayWord1 == ['c', 'a', 't']:
                            print(displayWord1)
                            print(' You have guessed the word')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
                        if incorrectChoice == 5:
                            print('You ran out of guesses')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0

                    # for 2nd word
                    while wordPicked == 2:
                        print('Your word has', (len(WordList[1])), 'letters good luck!')
                        print(displayWord2)
                        LetterGuessed = str(input('Guess a letter: '))

                        if LetterGuessed == 'd':
                            if displayWord2[0] == 'd':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'o':
                            if displayWord2[1] == 'o':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'g':
                            if displayWord2[2] == 'g':
                                print('why are you guessing a letter you already guessed :|')

                        if LetterGuessed == 'd':
                            print(LetterGuessed, 'is in the word')
                            displayWord2[0] = 'd'

                        if LetterGuessed == 'o':
                            print(LetterGuessed, 'is in the word')
                            displayWord2[1] = 'o'

                        if LetterGuessed == 'g':
                            print(LetterGuessed, 'is in the word')
                            displayWord2[2] = 'g'

                        if LetterGuessed != 'd' and LetterGuessed != 'o' and LetterGuessed != 'g':
                            print('incorrect choice sorry')
                            incorrectChoice = incorrectChoice + 1
                        if displayWord2 == ['d', 'o', 'g']:
                            print(displayWord2)
                            print(' You have guessed the word')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
                        if incorrectChoice == 5:
                            print('You ran out of guesses')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0

                    # for 3rd word
                    while wordPicked == 3:
                        print('Your word has', (len(WordList[2])), 'letters good luck!')
                        print(displayWord3)
                        LetterGuessed = str(input('Guess a letter: '))

                        if LetterGuessed == 'e':
                            if displayWord3[0] == 'e':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'a':
                            if displayWord3[1] == 'a':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 't':
                            if displayWord3[2] == 't':
                                print('why are you guessing a letter you already guessed :|')

                        if LetterGuessed == 'e':
                            print(LetterGuessed, 'is in the word')
                            displayWord3[0] = 'e'

                        if LetterGuessed == 'a':
                            print(LetterGuessed, 'is in the word')
                            displayWord3[1] = 'a'

                        if LetterGuessed == 't':
                            print(LetterGuessed, 'is in the word')
                            displayWord3[2] = 't'

                        if LetterGuessed != 'e' and LetterGuessed != 'a' and LetterGuessed != 't':
                            print('incorrect choice sorry')
                            incorrectChoice = incorrectChoice + 1
                        if displayWord3 == ['e', 'a', 't']:
                            print(displayWord3)
                            print(' You have guessed the word')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
                        if incorrectChoice == 5:
                            print('You ran out of guesses')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0

                    # for 4th word
                    while wordPicked == 4:
                        print('Your word has', (len(WordList[3])), 'letters good luck!')
                        print(displayWord4)
                        LetterGuessed = str(input('Guess a letter: '))

                        if LetterGuessed == 'b':
                            if displayWord4[0] == 'b':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'a':
                            if displayWord4[1] == 'a':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 't':
                            if displayWord4[2] == 't':
                                print('why are you guessing a letter you already guessed :|')

                        if LetterGuessed == 'b':
                            print(LetterGuessed, 'is in the word')
                            displayWord4[0] = 'b'

                        if LetterGuessed == 'a':
                            print(LetterGuessed, 'is in the word')
                            displayWord4[1] = 'a'

                        if LetterGuessed == 't':
                            print(LetterGuessed, 'is in the word')
                            displayWord4[2] = 't'

                        if LetterGuessed != 'b' and LetterGuessed != 'a' and LetterGuessed != 't':
                            print('incorrect choice sorry')
                            incorrectChoice = incorrectChoice + 1
                        if displayWord4 == ['b', 'a', 't']:
                            print(displayWord4)
                            print(' You have guessed the word')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
                        if incorrectChoice == 5:
                            print('You ran out of guesses')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0

                    # for 5th word
                    while wordPicked == 5:
                        print('Your word has', (len(WordList[4])), 'letters good luck!')
                        print(displayWord5)
                        LetterGuessed = str(input('Guess a letter: '))
                        if LetterGuessed == 'f':
                            if displayWord5[0] == 'f':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'a':
                            if displayWord5[1] == 'a':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 't':
                            if displayWord5[2] == 't':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'e':
                            if displayWord5[3] == 'e':
                                print('why are you guessing a letter you already guessed :|')
                        if LetterGuessed == 'f':
                            print(LetterGuessed, 'is in the word')
                            displayWord5[0] = 'f'

                        if LetterGuessed == 'a':
                            print(LetterGuessed, 'is in the word')
                            displayWord5[1] = 'a'

                        if LetterGuessed == 't':
                            print(LetterGuessed, 'is in the word')
                            displayWord5[2] = 't'

                        if LetterGuessed == 'e':
                            print(LetterGuessed, 'is in the word')
                            displayWord5[3] = 'e'

                        if LetterGuessed != 'f' and LetterGuessed != 'a' and LetterGuessed != 't' and LetterGuessed != 'e':
                            print('incorrect choice sorry')
                            incorrectChoice = incorrectChoice + 1
                        if displayWord5 == ['f', 'a', 't', 'e']:
                            print(displayWord5)
                            print(' You have guessed the word')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
                        if incorrectChoice == 5:
                            print('You ran out of guesses')
                            MainMenu = 'y'
                            MenuChoice = 0
                            wordPicked = 0
        break

    except:
        print('\nStop trying to break the program')
print('thanks for using my program')
