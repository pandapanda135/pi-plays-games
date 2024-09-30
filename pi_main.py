import os
import keyboard
from mpmath import mp
import time
from key_codes import *
from dotenv import load_dotenv, set_key
from pathlib import Path
import obs_websocket as obs

load_dotenv("up.env")
mp.dps = 5000 # Set decimal places

up = 0
button_hold_time = 0.25
start_time = 5 #change to modify how long until it start 
#handles loading 
env_file_path = Path("up.env")
new_up = os.getenv("UP")
if new_up != None:
    up = int(new_up)
else:
    set_key(dotenv_path=env_file_path, key_to_set="UP", value_to_set='0')

#update variables function
def update_up():
    global up
    up += 1

#countdown to start
while True:
    if start_time == 0:
        break
    else:
        pass
    print("starting in:", start_time)
    start_time -= 1
    time.sleep(1)

pi = str(mp.pi)
split_pi = list(pi)

#   Source Name: Colour Source | SceneItem ID: 5(dont use)
#   Source Name: Display Capture 3 | SceneItem ID: 6 (dont use)
#   Source Name: B_button_pressed.png | SceneItem ID: 10
#   Source Name: A_button_pressed.png | SceneItem ID: 19
#   Source Name: A_button_pressed | SceneItem ID: 11
#   Source Name: B_button | SceneItem ID: 9
#   Source Name: up_button_pressed.png | SceneItem ID: 20
#   Source Name: up_button | SceneItem ID: 15
#   Source Name: right_button_pressed.png | SceneItem ID: 21
#   Source Name: right_button | SceneItem ID: 16
#   Source Name: left_button_pressed.png | SceneItem ID: 22
#   Source Name: left_button | SceneItem ID: 17
#   Source Name: down_button_pressed.png | SceneItem ID: 23
#   Source Name: down_button | SceneItem ID: 18
#  Source Name: start_button_pressed.png | SceneItem ID: 30
#  Source Name: start_button | SceneItem ID: 25
#  Source Name: select_button_pressed.png | SceneItem ID: 31
#  Source Name: select_button | SceneItem ID: 26

while True:
    time.sleep(0.5) # change time between input if this is set to 0.25 it will take approx 0.5 seconds assuming button_hold_time is set to 0.25
    #use this if you want time between each input but cant increase key held time
    #switch to select key press
    match split_pi[up]:
        case '0':
            HoldAndReleaseKey(W, button_hold_time)
            obs.Toggle_obs(15,20,button_hold_time)
            print("w")
        case '1':
            HoldAndReleaseKey(A, button_hold_time)
            obs.Toggle_obs(17,22,button_hold_time)
            print("a")
        case '2':
            HoldAndReleaseKey(D, button_hold_time)
            obs.Toggle_obs(16,21,button_hold_time)
            print("d")
        case '3':
            HoldAndReleaseKey(S, button_hold_time)
            obs.Toggle_obs(18,23,button_hold_time)
            print("s")
        #not great for pokemon emerald can be enabled if playing other game
        # case '4':
        #     HoldAndReleaseKey(Z, button_hold_time)
        #     print("z")
        case '5'|'4':
            HoldAndReleaseKey(X, button_hold_time)
            obs.Toggle_obs(25,30,button_hold_time)
            print("x")
        case '6':
            HoldAndReleaseKey(E, button_hold_time)
            obs.Toggle_obs(11,19,button_hold_time)
            print("e")
        case '7':
            HoldAndReleaseKey(Q, button_hold_time)
            obs.Toggle_obs(9,10,button_hold_time)
            print("q")
        case '8':
            HoldAndReleaseKey(F, button_hold_time)
            print("f")
        case '9':
            HoldAndReleaseKey(R, button_hold_time)
            print("r")
        #deals with characters not defined
        case _:
            print("non")
    update_up()
    #handles saving
    env_up = str(up)
    set_key(dotenv_path=env_file_path, key_to_set="UP", value_to_set=env_up)
    #resets up if it is larger then decimal places to prevent crash
    if up >= mp.dps:
        up = 0
        print("pi reset")
    else:
        pass
    
    #find a way to improve this while keeping it all in one line on terminal
    print(up-5,"|",up-4,"|",up-3,"|",up-2,"|",up-1,"|",up,"|",up+1,"|",up+2,"|",up+3,"|",up+4,"|",up+5)
    
    if keyboard.is_pressed('e'):
        break
    else:
        pass