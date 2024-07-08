import random


def play_again():
    choice = input("Enter Y if you want to play again, or N if you want to exit")
    if choice.upper() == 'Y':
        print(
            "Please select your mode: \nType 1 for the computer to choose a word for you\nType 2 for you to choose a word yourself!\nType 3 to play a special word")
        mode = input("choose mode: ")
        mode_choice(mode)
    else:
        print("Thank you for playing today!")


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += '_' + " "
    return display


def display_hangman(attempts):
    stages = ["""
                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \
                    -
                """,
              """
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |     / 
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |     \|/
                  |      |
                  |      
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |     \|
                  |      |
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
              ]
    print(stages[attempts])


def the_game_at_its_core(chosen_word):
    attempts = 6
    list_chars = []
    for char in chosen_word:
        list_chars.append(char)
    # print(list_chars)

    print("lets begin!")
    print("""
                      --------
                      |      |
                      |      
                      |    
                      |      
                      |     
                      -
                  """)

    guessed_letters = []

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts -= 1
            print("Incorrect! Attempts left:", attempts)
            display_hangman(attempts)
            if attempts == 0:
                print("Sorry, you ran out of attempts. The word was:", chosen_word)
                play_again()
                break
        else:
            print("Correct!")

        word_display = display_word(chosen_word, guessed_letters)
        print(word_display)

        if '_' not in word_display:
            print("Congratulations! You guessed the word:", chosen_word)
            play_again()
            break


def compvsplayer():
    filename = "words.txt"
    with open(filename, 'r') as file:
        words = [word.strip() for word in file.readlines() if len(word.strip()) >= 5]
    chosen_word = random.choice(words)
    the_game_at_its_core(chosen_word.lower())


def playervsplayer():
    chosen_word = input("Input the word you want to set for the game: ")
    print(".\n.\n.\n.\nprocessing\n.\n.\n.\n.\n")
    the_game_at_its_core(chosen_word.lower())


def specialmode():
    chosen_word = "Python"
    the_game_at_its_core(chosen_word.lower())


print("Welcome to Hangman!")
print("This game has been created by Pihu Jha")
print("\n")
print(
    "Please select your mode: \nType 1 for the computer to choose a word for you\nType 2 for you to choose a word yourself!\nType 3 to play a special word")
mode = input("choose mode: ")


def mode_choice(mode):
    if mode == '1':
        compvsplayer()
    elif mode == '2':
        playervsplayer()
    elif mode == '3':
        specialmode()
    else:
        print("Please enter a valid mode")
        mode = input("choose mode: ")
        mode_choice(mode)


mode_choice(mode)
