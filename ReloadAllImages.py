# Coypright (c) 2021 Nidonocu
#
# See LICENCE file for details

bl_info = {
    "name": "Reload All Images",
    "blender": (2, 93, 0),
    "location": "File > Reload Images and Node Editor",
    "author": "Nidonocu",
    "category": "User Interface",
    "description": "Fetch all external image textures referenced within the Blend file, from their last saved disk version",
    "version": (1, 0, 0),
    "tracker_url": "https://github.com/Nidonocu/ReloadAllImages"
}

import bpy

class ReloadAll(bpy.types.Operator):
    """Fetch all external image textures from their last saved disk version"""
    bl_label = "Reload All Images"
    bl_icon = "OUTLINER_OB_IMAGE"
    bl_idname = "image.reload_all"
    bl_description = "Fetch all external image textures from their last saved disk version"
    
    def invoke(self, context, event):
        are_files_dirty = False

        for image in bpy.data.images:
            if (image.is_dirty):
                are_files_dirty = True
                
        if (are_files_dirty):
            return context.window_manager.invoke_confirm(self, event)
        return self.execute(context)
        
    def execute(self, context):
        for image in bpy.data.images:
            image.reload()
        self.report({'INFO'}, "All Textures Reloaded")
        return {'FINISHED'}

    
def menu_draw(self, context):
    self.layout.separator()
    self.layout.operator("image.reload_all", icon="OUTLINER_OB_IMAGE")

def register():
    bpy.utils.register_class(ReloadAll)
    bpy.types.TOPBAR_MT_file.append(menu_draw)
    bpy.types.NODE_HT_header.append(menu_draw)

def unregister():
    bpy.types.TOPBAR_MT_file.remove(menu_draw)
    bpy.types.NODE_HT_header.remove(menu_draw)
    bpy.utils.unregister_class(ReloadAll)

if __name__ == "__main__":
    register()
