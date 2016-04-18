#!/usr/bin/env python3

"""
fight_v2.py
Le newer fight script.

Created by Me. *

* Name has been witheld, in case the IT Techs see this.
    Hi, IT Techs. How's life?
    I'm good, thanks for asking!
"""


import os
from random import randrange, shuffle
from time import time


# Add more names here. Encase names in ""s and add "," to end of each value.
names = [
"Salim",
"Ismail",
"Tanwir",
"Zainab",
"Tiana",
"Imran",
"Nathan",
"Amrit",
"Issy",
"Nyla",
"Bilal",
"Natalia",
"Janithaa",
"Rahul",
"Ariana",
"Sarmad",
"Ridhi",
"Neel",
"Joseph",
"Emily O",
"Chris",
"Shabazz",
"Naveena",
"Ramin",
"Ali",
"Malaika",
"Nikita",
"Zaynah",
"Arif",
"Aroma",
"Damanjeet",
"Emily K",
"Hardeep",
"Harkiran",
"Jimeet",
"Kajal",
"Karanjeet",
"Karolina",
"Khizar",
"Manav",
"Nishi",
"Rifah",
"Rovena",
"Salina",
"Simranjeet S",
"Swathiga",
"Yassar",
"Zahra",
"Zarak"
]

# Do le shuffle...
shuffle(names)


# CMD TOOLS.
def _clear():
    os.system("cls")
    return None
def _change_title(new_title):
    os.system("title " + new_title)
    return None
def _pause():
    if "pyscripter" in globals():
        input("Press [ENTER] to exit.")
    else:
        os.system("pause")

# Prettify le Question, because people are too lazy with punctuation.
def _prettify_question(question):
    pretty_q = question[0].capitalize() + question[1:]
    if pretty_q[-1] is not "?":
        pretty_q += "?"
    return pretty_q

# Generate name and combination from "names" array.
# * Could've condensed this into one function, but meh.
# * Debugging is easier this way.
def generate_name():
    rand_num = randrange(len(names))
    return names[rand_num]
def generate_combination():
    person_1 = generate_name()
    person_2 = generate_name()
    return [person_1, person_2]


# Set up le variables...
# You may touch the next line. Nothing after. Okay?
question = "Who would win in a fight?"
orig_q = question


while True:  # Infinite looooop.
    # Clear le screen at beginning of loop, to make my life easier.
    _clear()
    _change_title("Enter time in seconds.")
    # * If you've encountered an error after the below, you obviously
    # * can't tell the difference between an int and a str.
    # * :P
    usr_tm = int(input("Enter time in seconds (Press 0 to edit text): "))
    if usr_tm == 0:
        # Change default text.
        _clear()
        _change_title("Enter custom text.")
        usr_q = input("Enter custom text (Press 0 to return text to default): ")
        # Yeah, I like zeroes. So pwetty...
        if usr_q == "0":
            usr_q = orig_q
        question = _prettify_question(usr_q)
        # Next iteration of le infinite loop!
        continue
    # Actual name stuff starts here.
    start_tm = time()
    # Change title.
    _change_title("Generating combination...")
    # Change combination count to 0...
    comb_count = 0
    # While time elapsed is lower than user inputted time...
    while (time() - start_tm) < usr_tm:
        _clear()
        # * Cue the pretty flickering effect...
        # * Woooooooooooooooooooooooooooo!
        print("Generating combination...", end="\n\n")
        combination = generate_combination()
        print(combination[0], "or", combination[1])
        # Probably a better way of doing this. I'm too lazy to research.
        comb_count += 1
    # After elapsed time > user inputted time...
    # * This is not entirely random, but is using the last combination
    # * generated in the "while" loop above. This should suffice.
    # * (Unless you're crazy enough to program atom decay
    # * into this program).
    _clear()
    # Purely for aesthetic reasons.
    _change_title("Combination Generated. (" + str(comb_count) + ")")
    # * Display the end result. To the end user, it would look like
    # * the text at the top has changed.
    # * However, this is not possible in this stupid language,
    # * so this'll have to suffice.
    # * (Hang on, is "this'll" a word (or contraction of)?)
    print(question, end="\n\n")
    print(combination[0], "or", combination[1], end="\n\n")
    _pause()
    # End of "while" loop.

# * This'll never be run, but I'll chuck it in there anyway.
# * Coz why not?
exit()

# EOF.