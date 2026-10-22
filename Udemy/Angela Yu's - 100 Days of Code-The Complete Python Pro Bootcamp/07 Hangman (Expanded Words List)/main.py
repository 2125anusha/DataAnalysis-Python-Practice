import random
from hangman_art import stages
from hangman_words import word_list

random_word=random.choice(word_list)

# To display the updated blank and filled letters
guessed_word=["_"] * len(random_word)
print(''.join(guessed_word))

lives=6
while lives>0:
    user_input = input("Type a letter: ")
    if user_input in guessed_word:
        print(f"You already guessed this letter: '{user_input}', pick another letter")

    for index in range(len(random_word)):
        if random_word[index]==user_input:
            guessed_word[index] = user_input

    if user_input not in random_word:
        lives -= 1
        print("Wrong! your lives left: ", lives)
        print(stages[lives])

    if lives<=0:
        print("You lose :(")
        print("The word was: ",random_word)
        break

    if "_" not in guessed_word:
        print("You win! ")
        print("Congratulations, the word is: ", random_word)
        break

    print(''.join(guessed_word))
