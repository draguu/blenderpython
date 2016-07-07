
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
'''
bl_info = {
    "name": "Scene Lighting Presets",
    "author": "meta-androcto",
    "version": (0,1),
    "blender": (2, 63, 0),
    "location": "View3D > Tool Shelf > Scene Lighting Presets",
    "description": "Creates Scenes with Lighting presets",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/Scripts/",
    "tracker_url": "",
    "category": "Object"}
'''

import bpy
import mathutils
import math
from math import pi
from bpy.props import *
from mathutils import Vector


class add_scene(bpy.types.Operator):
    bl_idname = "plane.add_scene"
    bl_label = "Create test scene"
    bl_description = "Scene with 'infinite' plane"
    bl_register = True
    bl_undo = True

    def execute(self, context):
        blend_data = context.blend_data
        ob = bpy.context.active_object

# add new scene
        bpy.ops.scene.new(type="NEW")
        scene = bpy.context.scene
        scene.name = "scene_plane"
# render settings
        render = scene.render
        render.resolution_x = 1920
        render.resolution_y = 1080
        render.resolution_percentage = 50
# add new world
        world = bpy.data.worlds.new("Plane_World")
        scene.world = world
        world.use_sky_blend = True
        world.use_sky_paper = True
        world.horizon_color = (0.004393, 0.02121, 0.050)
        world.zenith_color = (0.03335, 0.227, 0.359)
        world.light_settings.use_ambient_occlusion = True
        world.light_settings.ao_factor = 0.25
# add camera
        bpy.ops.object.camera_add(location=(7.48113, -6.50764, 5.34367), rotation=(1.109319, 0.010817, 0.814928))
        cam = bpy.context.active_object.data
        cam.lens = 35
        cam.draw_size = 0.1
        bpy.ops.view3d.viewnumpad(type='CAMERA')
# add point lamp
        bpy.ops.object.lamp_add(type="POINT", location=(4.07625, 1.00545, 5.90386), rotation=(0.650328, 0.055217, 1.866391))
        lamp1 = bpy.context.active_object.data
        lamp1.name = "Point_Right"
        lamp1.energy = 1.0
        lamp1.distance = 30.0
        lamp1.shadow_method = "RAY_SHADOW"
        lamp1.use_sphere = True
# add point lamp2
        bpy.ops.object.lamp_add(type="POINT", location=(-0.57101, -4.24586, 5.53674), rotation=(1.571, 0, 0.785))
        lamp2 = bpy.context.active_object.data
        lamp2.name = "Point_Left"
        lamp2.energy = 1.0
        lamp2.distance = 30.0
#        lamp2.shadow_method = "RAY_SHADOW"

# light Rim
        """
        # add spot lamp3
        bpy.ops.object.lamp_add(type="SPOT", location = (0.191,0.714,0.689), rotation =(0.891,0,2.884))
        lamp3 = bpy.context.active_object.data
        lamp3.name = "Rim Light"
        lamp3.color = (0.194,0.477,1)
        lamp3.energy = 3
        lamp3.distance = 1.5
        lamp3.shadow_buffer_soft = 5
        lamp3.shadow_buffer_size = 4096
        lamp3.shadow_buffer_clip_end = 1.5
        lamp3.spot_blend = 0.5
        """

# add plane

        bpy.ops.mesh.primitive_plane_add(radius=50, view_align=False, enter_editmode=False, location=(0, 0, -1))

        bpy.ops.transform.rotate(value=-0.8, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        plane = bpy.context.active_object
# add new material

        planeMaterial = blend_data.materials.new("Plane_Material")
        bpy.ops.object.material_slot_add()
        plane.material_slots[0].material = planeMaterial


# Material settings
        planeMaterial.preview_render_type = "CUBE"
        planeMaterial.diffuse_color = (0.2, 0.2, 0.2)
        planeMaterial.specular_color = (0.604, 0.465, 0.136)
        planeMaterial.specular_intensity = 0.3
        planeMaterial.ambient = 0
        planeMaterial.use_cubic = True
        planeMaterial.use_transparency = False
        planeMaterial.alpha = 0
        planeMaterial.use_transparent_shadows = True
        return {"FINISHED"}


class INFO_MT_add_scenesetup(bpy.types.Menu):
    bl_idname = "INFO_MT_plane.add_scene"
    bl_label = "Lighting Setups"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("plane.add_scene",
                        text="Add scene")

#### REGISTER ####


def add_object_button(self, context):
    self.layout.menu("INFO_MT_plane.add_scene", icon="PLUGIN")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_add.remove(add_object_button)


if __name__ == '__main__':
    register()
