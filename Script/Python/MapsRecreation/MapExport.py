# Should be used with UE 4.12 version of EC with the plugin: https://github.com/20tab/UnrealEnginePython

import unreal_engine as ue
import json


final_result = []
actors = ue.editor_get_selected_actors()


def get_fvector_data(fvector):
    return fvector.x, fvector.y, fvector.z


def get_frotator_data(frotator):
    return frotator.pitch, frotator.roll, frotator.yaw


for actor in actors:
    try:
        comp = actor.components()[0]
        static_mesh_path = comp.StaticMesh.get_full_name()
        loc = get_fvector_data(actor.get_actor_location())
        rot = get_frotator_data(actor.get_actor_rotation())
        scale = get_fvector_data(actor.get_actor_scale())
        result = {"loc": loc, "rot": rot, "scale": scale}
        final_result.append({"path": static_mesh_path, "transform": result})
    except:
        continue

with open("zedek1_main.json", "w") as file:
    json.dump(final_result, file)