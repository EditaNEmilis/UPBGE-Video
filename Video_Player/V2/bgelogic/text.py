# Packages
import bge

# Function
def Main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = bge.logic.getCurrentScene()
    frameText = scene.objects["FrameText"]
    aspectText = scene.objects["AspectText"]
    
    aspectRat = {
        1: "1:1",
        2: "4:3",
        3: "16:9"
    }
    
    frameText["Text"] = "FRAMES: " + str(own["Offset"])
    aspectText["Text"] = "ASPECT: " + str(aspectRat[own["Aspect"]])
    ###
    
Main()