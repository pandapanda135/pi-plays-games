import keyboard
from mpmath import mp
import time
from key_codes import *

mp.dps = 5000 # Set decimal places

up = 0
#update variables function
def update_up():
    global up
    up += 1

while True:
    time.sleep(0.5)
    pi = str(mp.pi)
    split_pi = list(pi)
    #switch to select key press
    match split_pi[up]:
        case '0':
            HoldAndReleaseKey(W, 1)
            update_up()
            print("w")
            pass
        case '1':
            HoldAndReleaseKey(A, 1)
            update_up()
            print("a")
            pass
        case '2':
            HoldAndReleaseKey(D, 1)
            update_up()
            print("d")
            pass
        case '3':
            HoldAndReleaseKey(S, 1)
            update_up()
            print("s")
            pass
        # case '4': this is just annoying
        #     HoldAndReleaseKey(Z,0.1)
        #     update_up()
        #     print("z")
        #     pass
        case '5'|'4':
            HoldAndReleaseKey(X,0.1)
            update_up()
            print("x")
            pass
        case '6':
            HoldAndReleaseKey(E,0.1)
            update_up()
            print("e")
            pass
        case '7':
            HoldAndReleaseKey(Q,0.1)
            update_up()
            print("q")
            pass
        case '8':
            HoldAndReleaseKey(F,0.1)
            update_up()
            print("f")
            pass
        case '9':
            HoldAndReleaseKey(R,0.1)
            update_up()
            print("r")
            pass
        #deals with characters not defined
        case _:
            update_up()
            print("non")
            pass
    if keyboard.is_pressed('e'):
        break
    else:
        pass
    #old code here incase issues
        # if split_pi[up] == '2':
    #     keyboard.press_and_release(W, 1)
    #     print("works")
    #     up += 1
    #     test += 1
    #     int_amount += 1
    #     pass
    # elif split_pi[up] == '3':
    #     keyboard.press_and_release(A, 1)
    #     print("works")
    #     up += 1
    #     test += 1
    #     int_amount += 1
    #     pass
    # elif split_pi[up] == '4':
    #     keyboard.press_and_release(S, 1)
    #     print("works")
    #     up += 1
    #     test += 1
    #     int_amount += 1
    #     pass
    # elif split_pi[up] == '5':
    #     keyboard.press_and_release(D, 1)
    #     print("works")
    #     up += 1
    #     test += 1
    #     int_amount += 1
    #     pass
    # else:
    #     up += 1
    #     print(":(", test)
    #     test += 1
    #     sad_amount += 1
    #     pass