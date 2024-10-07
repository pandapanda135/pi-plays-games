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
def countdown():
    global start_time
    while True:
        if start_time == 0:
            start_time = 5
            break
        else:
            pass
        print("starting in:", start_time)
        start_time -= 1
        time.sleep(1)

def pause():
    print("script is now paused press X to close or press H to continue")
    while True:
        if keyboard.is_pressed("h"):
            main()
        if keyboard.is_pressed('x'):
            break

def saving():
    global up
    #handles saving
    env_up = str(up)
    set_key(dotenv_path=env_file_path, key_to_set="UP", value_to_set=env_up)

pi = str(mp.pi)
split_pi = list(pi)
# I recomend replaceing these with your own 
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

def main():
    global split_pi
    global up
    global dps
    countdown()
    while True:
        time.sleep(0.5) # change time between input if this is set to 0.25 it will take approx 0.5 seconds assuming button_hold_time is set to 0.25
        #use this if you want time between each input but cant increase key held time
        #switch to select key press
        match split_pi[up]:
            case '0':
                key_select = W
                obs_not_select = 15
                obs_select = 20
                print("w",split_pi[up])
            case '1':
                key_select = A
                obs_not_select = 17
                obs_select = 22
                print("a",split_pi[up])
            case '2':
                key_select = D
                obs_not_select = 16
                obs_select = 21
                print("d",split_pi[up])
            case '3':
                key_select = S
                obs_not_select = 18
                obs_select = 23
                print("s",split_pi[up])
            #not great for pokemon emerald can be enabled if playing other game
            # case '4':
            #     HoldAndReleaseKey(Z, button_hold_time)
            #     print("z")
            case '5'|'4':
                key_select = X
                obs_not_select = 25
                obs_select = 30
                print("x",split_pi[up])
            case '6':
                key_select = A
                obs_not_select = 11
                obs_select = 19
                print("a",split_pi[up])
            case '7':
                key_select = B
                obs_not_select = 9
                obs_select = 10
                print("b",split_pi[up])
            case '8':
                key_select = F
                #temp until added to obs
                time.sleep(button_hold_time)
                print("f",split_pi[up])
            case '9':
                key_select = R
                time.sleep(button_hold_time)
                print("r",split_pi[up])
            #deals with characters not defined
            case _:
                obs_not_select = 0
                obs_select = 0
                print("non")
        update_up()
        saving()
        HoldAndReleaseKey(key_select, button_hold_time)
        obs.Toggle_obs(obs_not_select,obs_select,button_hold_time)
        #resets up if it is larger then decimal places to prevent crash
        if up >= mp.dps:
            up = 0
            print("pi reset")
        else:
            pass
        
        #find a way to improve this while keeping it all in one line on terminal
        print(up-5,"|",up-4,"|",up-3,"|",up-2,"|",up-1,"|",up,"|",up+1,"|",up+2,"|",up+3,"|",up+4,"|",up+5)
        
        if keyboard.is_pressed('e'):
            pause()
            break
        else:
            pass

main()