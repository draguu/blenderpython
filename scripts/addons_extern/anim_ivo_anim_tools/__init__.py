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

#
#  Written by Ivo Grigull
#  http://ivogrigull.com
#  http://character-rigger.com
#

bl_info = {
    "name": "Ivo Animation Toolbox",
    "author": "Ivo Grigull (Loolarge)",
    "version": (0, 1),
    "blender": (2, 5, 7),
    "api": 34470,
    "location": "Toolbar in pose mode",
    "description": "Collection of animation helper tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Animation"}


if "bpy" in locals():
    import imp
    imp.reload(ivo_anim_tools)
    imp.reload(ivo_jogwheel)
    #~ imp.reload(menu)
    imp.reload(ivo_selection_sets)
else:
    from . import ivo_anim_tools
    from . import ivo_jogwheel
    #~ from . import menu
    from . import ivo_selection_sets  # menu

import bpy
import bpy_types


#~ import space_info


def register():

    bpy.utils.register_module(__name__)
    #~ if bpy.app.build_platform.find("Windows") != -1:
    #~ ivo_anim_tools.register()
    #~ ivo_jogwheel.register()
    #~ ivo_selection_sets.register()
    #~ menu.register()


def unregister():
    bpy.utils.unregister_module(__name__)
    #~ ivo_anim_tools.unregister()
    #~ ivo_jogwheel.unregister()
    #~ menu.register()
    #~ ivo_selection_sets.unregister()
    pass

if __name__ == "__main__":
    register()
