# Packages
import bge, bpy

# Function
def Main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    keyboard = bge.logic.keyboard
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
    
    # Material Data
    bpy.data.materials["Video"].node_tree.nodes["Image Texture"].image_user.use_cyclic = True # Init
    bpy.data.materials["Video"].node_tree.nodes["Image Texture"].image_user.use_auto_refresh = True # Init
    bpy.data.materials["Video"].node_tree.nodes["Image Texture"].image_user.frame_offset = own["Offset"]
    
    # Clamp
    if own["Offset"] < 0:
        own["Offset"] = 0

    ###
    # Play/Pause
    if JUST_ACTIVATED in keyboard.inputs[bge.events.SPACEKEY].queue:
        if own["Playing"] == True:
            own["Playing"] = False
        else:
            own["Playing"] = True
            
    if own["Playing"] == True and own["Reverse"] == False:
        own["Offset"] += 1
    else:
        own["Offset"] = own["Offset"]
        
    # Reverse
    if JUST_ACTIVATED in keyboard.inputs[bge.events.TKEY].queue:
        if own["Reverse"] == True:
            own["Reverse"] = False
        else:
            own["Reverse"] = True
            
    if own["Reverse"] == True:
        own["Offset"] -= 1
        
    # Restart
    if JUST_ACTIVATED in keyboard.inputs[bge.events.RKEY].queue:
        own["Offset"] -= own["Offset"]
    ###
    
Main()