import sys
import sqlite3

def get_word():
    db = sqlite3.connect('words.db')
    cursor = db.cursor()
    try:
        cursor.execute("SELECT Word FROM WORDS ORDER BY random() LIMIT 1")
    except sqlite3.OperationalError as err:
        print("Error Occured while accessing database:",err,end=" ")
        sys.exit(1)
    word = cursor.fetchone()[0]
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letter = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letter:
                print("You have already guessed the letter",guess)
            elif guess not in word :
                print(guess, "is not in the word")
                tries -= 1
                guessed_letter.append(guess)
            else:
                print("Great!", guess,"is in the word..you did it ..!!" )
                guessed_letter.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                  word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the letter", guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                 guessed = True
                 word_completion = word
        else:
              print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
       print("Congratulations! You got the correct word! You won!!")
    else:
        print("Sorry! You ran out of tries, The word  was " + word + " .Try next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
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
    return stages[tries]

def main():
    while True:
        play(get_word())
        if input("Play Again? (Y/N) ").upper() == "N":
            break

if __name__ == "__main__":
    main()