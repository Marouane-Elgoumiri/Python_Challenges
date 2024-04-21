import random

lisr=["Tangier", "Algiers", "Tunis", "Tripoli", "Alalamain","Jaffa", "Damascus","Samarra", "Baku","Rostov","Murmansk", "Narvik","Oslo", "Kiel"]
word = random.choice(lisr).lower()
guessed_letters = []


def askLetter():
    print("This below is the letter go ahead and guess a letter")
    for j in range(len(word)):
        print("-",end=" ")

def display_word(word, guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display +="_"
    return display
def play():
    hp = len(word)  
    while hp > 0: 
        letter = input("\nEnter a letter: ")
        if len(letter) != 1:
            print("Enter a single letter! ")
            continue
        
        if letter in guessed_letters:
            print("You have already guessed that letter")
            continue
        guessed_letters.append(letter)  

        if letter in word:
            print(f"Nice you got one! {display_word(word, guessed_letters)}")
            if "_" not in display_word(word, guessed_letters):  
                print("****************************************************************")
                print(f"********Congratulations! You guessed it right! {word}******************")
                print("****************************************************************")
                break
        else:
            hp -= 1  
            print(f"Nope, you lose 1❤️, you have {hp} left ")
            
    if hp == 0:
        print(f"WASTED! you failed\n the word was {word}")     


if __name__ == "__main__":
    print("*****************************************Hello to the Hangman game****************************************************")
    print("You have to guess a word by entering a letter\n each time you enter a letter we'll check if you guessed it right ot no")
    print("**********************************************************************************************************************")
    print(f"\nBEWARE! you have only {len(word)}❤️ if you run out of HP you lose")
    askLetter()
    play()