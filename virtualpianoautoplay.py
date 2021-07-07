# made by weirdboi12408

import time
import timeit
import keyboard
import random

#data

notes = "abcdefghijklmnopqrstuvwxyz1234567890"

# functions

def playnote(note):
    global notevariability
    global notemistakes
    if notemistakes == True and random.randint(0,notevariability) == 0:
        global notes
        x = random.randint(0,len(notes) - 1)
        keyboard.press(x)
        keyboard.release(x)
    else:
        if note.isupper() == True:
            keyboard.press("shift")
        keyboard.press(note)
        keyboard.release(note)
        if note.isupper() == True:
            keyboard.release("shift")
    print(note)
def createrandom(amount):
    global timingvariability
    global minus
    minus = (0 - (random.randint(0,100) / amount)) * timingvariability
#testing

#t = timeit.default_timer()
#keyboard.press(" ")
#minus = timeit.default_timer() - t
#print(minus)
minus = 0

#actual code

#song chooser
q = input("what song to play")
try:
    song = list(open('pianosongs'))[int(q)]
    n = list(open('pianosongsbpm'))[int(q)]
except ValueError:
    song = q
    n = input("What bpm")
try:
    wait = 15 / int(n)
except ValueError:
    wait = 0.1

#human

if input("timing mistakes? (y/n)").upper() == "Y":
    timingmistakes = True
    try:
        timingvariability = int(input("timing variability?"))
    except ValueError:
        timingvariability = 1
else:
    timingmistakes = False
if input("note mistakes? (y/n)").upper() == "Y":
    notemistakes = True
    try:
        notevariability = int(input("note variability?"))
    except ValueError:
        notevariability = 15
else:
    notemistakes = False

#song

if minus >= wait:
    wait = 0
    minus = 0
print("wt: " + str(wait) + "\nmt: " + str(minus))
time.sleep(5)
n = 0
while n < len(song):
    if song[n] == " ":
        print(" ")
        time.sleep(wait - minus)
    elif song[n] == "|":
        print(" --- ")
        time.sleep((wait * 4) - minus)
    elif song[n] == "[":
        n = n + 1
        while song[n] != "]":
            if timingmistakes == True:
                createrandom(3000)
                time.sleep(0 - minus)
            playnote(song[n])
            n = n + 1
        time.sleep(wait - minus)
    else:
        playnote(song[n])
        time.sleep(wait - minus)
    n = n + 1
    if timingmistakes == True:
        createrandom(1000)

print("finished")
