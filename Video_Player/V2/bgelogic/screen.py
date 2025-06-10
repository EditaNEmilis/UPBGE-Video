# Packages
import bge

# Function
def Main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = bge.logic.getCurrentScene()
    plane = scene.objects["Plane"]
    
    keyboard = bge.logic.keyboard
    JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED
    
    sizeX = {
        1: "1.0",
        2: "1.333",
        3: "1.920"
    }
    
    sizeY = {
        1: "1.0",
        2: "1.0",
        3: "1.080"
    }

    ###
    # Aspect Ratios
    if JUST_ACTIVATED in keyboard.inputs[bge.events.AKEY].queue:
        if own["Aspect"] < 3:
            own["Aspect"] += 1
        else:
            own["Aspect"] = 1
            
        plane.worldScale.x = float(sizeX[own["Aspect"]])
        plane.worldScale.y = float(sizeY[own["Aspect"]])
    ###
    
Main()