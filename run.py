"""import gspread
from google.oauth2.service_account import credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')

words = SHEET.worksheet('words')

data = words.get_all_values()
print(data)"""
import keyboard
import random
# Start game loop press instructions or start game
welcome = input("Welcome to Python Wordl game! For instructions press 'i' To play game press 'p'")
while welcome:
    if keyboard.is_pressed("p"):
        break

    if keyboard.is_pressed("i"):
        print(" Start by typing in a five-letter word. If any of the letters in the word you typed in show up as green, they’re in the word and in that same exact position. For example, if you type in “Walks” and the word of the day is “Sable,” the letter A would light up as green.If any of the letters in the word you typed show up as yellow, that means they’re in the word — but their placement doesn’t correspond to the letter’s position in the final word. Using the example above, the letters S and L would show up as yellow, since they’re in “Sable,” but not in the right spot in the word.You have 6 tries to guess the word before the game is over, so take your time and really think.")


# input loop with the player guess only take 5 letters string else throw error
guess = input('please guess a 5 letter word') 
if len(guess) > 5:
    print("\033[1;31;40m Your word is too long, only 5 letters please!\n")
elif len(guess) < 5:
    print("\033[1;31;40m Your word is too short, 5 letters please!\n")
    

# list of 5 letter words from websters
words = ['tasty', 'about', 'above', 'actor', 'abuse']

# function that chooses random word from the words list
word = random.choice(words)
