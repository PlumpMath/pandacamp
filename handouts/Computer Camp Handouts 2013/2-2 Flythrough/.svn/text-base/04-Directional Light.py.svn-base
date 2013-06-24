from Panda import *

#Static models and behaviors
camera.position = P3(0, 0, 7)
d = discoHall(position = P3(0, 50, 0), hpr = HPR(pi/2, 0, 0))

# This puts the panda on the stage
p = panda(position = P3(0, 60, 3), size = 3)

#control RGB of point light
PLColor = sliderColor(label="DL Color")

dlh = slider(max = 10, min = 0, label="DL heading")
dlp = slider(max = 10, min = 0, label="DL pitch")

dl = directionalLight(color = PLColor, hpr = HPR(dlh,dlp,0) )

# The disco is completely white - without directional light it's invisible!
# Note how the directional light works - surfaces that face the same way
# get identical illumination.

start()

