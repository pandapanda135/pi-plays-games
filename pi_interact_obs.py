import obspython as obs


def toggle(self):
    current_scene = obs.obs_scene_from_source(obs.obs_frontend_get_current_scene())
    scene_item = obs.obs_scene_find_source(current_scene, self.source_name)
    boolean = not obs.obs_sceneitem_visible(scene_item)
    obs.obs_sceneitem_set_visible(scene_item, boolean)