import obsws_python as obs
import time
import toml

scene_name = "Scene 6"
#commented as cant get it working :')
#cl = toml.load("config.toml")

# pass conn info if not in config.toml
#add websocket settings in the function
cl = obs.ReqClient()

def Toggle_obs(not_pressed, pressed, seconds):
    #hide off enables on then waits, second hides on enables off
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=not_pressed,enabled=False)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=pressed,enabled=True)
    time.sleep(seconds)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=pressed,enabled=False)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=not_pressed,enabled=True)