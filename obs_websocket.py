import obsws_python as obs
import time
import toml

scene_name = "Scene 6"
scene_item_id = 0
#commented as cant get it working :')
#cl = toml.load("config.toml")

# pass conn info if not in config.toml
cl = obs.ReqClient()

resp = cl.get_scene_item_list("Scene 6")

print("version",resp.scene_items)

#cl.set_scene_item_enabled(scene_name="Scene 6",item_id=1,enabled=False)
#cl.set_scene_item_enabled(scene_name="Scene 6",item_id=4,enabled=True)


def Toggle_obs(not_pressed, pressed, seconds):
    #hide off enables on then waits, second hides on enables off
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=not_pressed,enabled=False)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=pressed,enabled=True)
    time.sleep(seconds)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=pressed,enabled=False)
    cl.set_scene_item_enabled(scene_name=scene_name,item_id=not_pressed,enabled=True)