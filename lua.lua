# this is used as a script in obs to get the sceneitemid of each source in your scene 
obs = obslua

function get_scene_item_ids(scene_name)
    local scene_source = obs.obs_get_source_by_name("Scene 6")
    local scene = obs.obs_scene_from_source(scene_source)
    local items = obs.obs_scene_enum_items(scene)

    for _, scene_item in ipairs(items) do
        local source = obs.obs_sceneitem_get_source(scene_item)
        local scene_item_id = obs.obs_sceneitem_get_id(scene_item)
        local source_name = obs.obs_source_get_name(source)
        print("Source Name: " .. source_name .. " | SceneItem ID: " .. scene_item_id)
    end

    obs.sceneitem_list_release(items)
    obs.obs_source_release(scene_source)
end

get_scene_item_ids("Scene 6")
