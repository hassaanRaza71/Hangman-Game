    #Step 2
logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    

                      '''
print(logo)
import random
hangman_words = [
        "apple", "banana", "grape", "orange", "watermelon", "strawberry",
        "elephant", "giraffe", "kangaroo", "dolphin", "panda", "penguin",
        "house", "apartment", "building", "school", "library", "hospital",
        "python", "computer", "keyboard", "mouse", "screen", "internet",
        "pizza", "burger", "pasta", "salad", "sushi", "sandwich",
        "happy", "sad", "angry", "excited", "bored", "nervous",
        "winter", "spring", "summer", "autumn", "season", "holiday",
        "mountain", "river", "forest", "desert", "ocean", "valley",
        "book", "magazine", "newspaper", "notebook", "diary", "novel",
        "music", "guitar", "piano", "violin", "drums", "flute",
        "dog", "cat", "rabbit", "hamster", "parrot", "fish",
        "circle", "square", "triangle", "rectangle", "oval", "hexagon",
        "red", "blue", "green", "yellow", "purple", "orange",
        "car", "bicycle", "train", "airplane", "boat", "motorcycle",
        "rain", "snow", "thunder", "lightning", "wind", "cloud",
        "king", "queen", "prince", "princess", "knight", "dragon",
        "friend", "family", "teacher", "doctor", "nurse", "police",
        "city", "village", "country", "continent", "island", "desert",
        "game", "puzzle", "riddle", "challenge", "adventure", "mystery",
        "travel", "journey", "explore", "discover", "adventure", "voyage",
        "history", "geography", "science", "math", "art", "literature",
        "garden", "flower", "tree", "grass", "bush", "shrub",
        "light", "dark", "bright", "dim", "shadow", "glow",
        "smile", "laugh", "cry", "frown", "scream", "whisper",
        "run", "walk", "jump", "swim", "fly", "crawl",
        "happy", "sad", "angry", "excited", "bored", "nervous",
        "strong", "weak", "brave", "scared", "calm", "anxious"]
chosen_word = random.choice(hangman_words)

    #Testing code
    #print(f'Pssst, the solution is {chosen_word}.')

    #TODO-1: - Create an empty List called display.
    #For each letter in the chosen_word, add a "_" to 'display'.
    #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

display=[]
for alpha in chosen_word:
    display+="_"
print(display)
lives=6
lost=False
while display.count("_")!=0 and lost==False:
    index=display.count("_")
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("You have already guessed this letter")
        print(display)
        continue
    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for alphabet in range(0,len(chosen_word)):
        if chosen_word[alphabet]==guess:
            display[alphabet]=guess

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    if index==display.count('_'):
        print(f"You have guessed {guess}, thats not in the word!. You lose a life." )
        print(stages[lives])
        lives-=1
    else:
        print("You have guessed Right!" )
    print(display)
        #print(lives)
    if lives==-1:
        lost=True
        print("You lost")
    elif "_" not in display:
        print("You Win")

