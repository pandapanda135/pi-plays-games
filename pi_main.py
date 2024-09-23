import keyboard
from mpmath import mp
import time
from key_codes import *

mp.dps = 3 # Set decimal places

up = 0
#update variables function
def update_up():
    global up
    up += 1

while True:
    time.sleep(0.5) # change time between input
    pi = str(mp.pi)
    split_pi = list(pi)
    #switch to select key press
    match split_pi[up]:
        case '0':
            HoldAndReleaseKey(W, 0.5)
            update_up()
            print("w")
        case '1':
            HoldAndReleaseKey(A, 0.5)
            update_up()
            print("a")
        case '2':
            HoldAndReleaseKey(D, 0.5)
            update_up()
            print("d")
        case '3':
            HoldAndReleaseKey(S, 0.5)
            update_up()
            print("s")
        #not great for pokemon emerald can be enabled if playing other game
        # case '4':
        #     HoldAndReleaseKey(Z,0.1)
        #     update_up()
        #     print("z")
        case '5'|'4':
            HoldAndReleaseKey(X,0.1)
            update_up()
            print("x")
        case '6':
            HoldAndReleaseKey(E,0.1)
            update_up()
            print("e")
        case '7':
            HoldAndReleaseKey(Q,0.1)
            update_up()
            print("q")
        case '8':
            HoldAndReleaseKey(F,0.1)
            update_up()
            print("f")
        case '9':
            HoldAndReleaseKey(R,0.1)
            update_up()
            print("r")
        #deals with characters not defined
        case _:
            update_up()
            print("non")
    #resets up if it is larger then decimal places to prevent crash
    if up >= mp.dps:
        up = 0
        print("pi reset")
    else:
        pass
    
    if keyboard.is_pressed('e'):
        break
    else:
        pass