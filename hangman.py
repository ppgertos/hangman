#!/bin/python3
import re
import time

import random

words = ["screwdriver","boat","carbine","strawberry","tree","bicycle"]
winning_phrases = ["Congrats You have won!!", "Hey, how did You do that?!","Wow, splendid, You did it!"]

def intro():
    print("Welcome to Gertos's hangman.")
    print("We start in:")
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Let's guess!")

def read_letter(chances):
    global guessed_letters
    need_letter = True
    while need_letter:
        letter = input("You have "+str(chances)+" chances left. Give a letter:")
        if re.match(r"[\w]",letter):
            if letter in guessed_letters:
                print('That letter You have already tried!')
            else:
                need_letter = False
    return letter

if __name__ == "__main__":
    intro()
    while True:
        secret = random.choice(words)
        fail_chars = len(secret)
        chances = 10
        guessed_letters = []
        while fail_chars > 0 and chances > 0:
            print("The secret is:")
            disp = ""
            fail_chars = 0
            for char in secret:
                if char in guessed_letters:
                    disp += char
                else:
                    disp += "."
                    fail_chars += 1
            print(disp)
            if fail_chars == 0:
                print(random.choice(winning_phrases))
                print()
                break
            lt = read_letter(chances)
            if lt in secret:
                print(lt +" is in secret word!")
            else:
                chances -= 1
                if chances > 0:
                    print("Try another one...")
            guessed_letters += lt

