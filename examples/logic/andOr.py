from Panda import *

# The "&" symbol means "and" and "|" means "or"
# So (x > 2) & (y > 3) would true if x is greater than 2 and y is greater than 3
# The parenthesis are needed to make sure that it does the > before the &

# This demonstrates "&" and "|" by clicking and dragging the panda changes
# color based on the corodinates on the screen in the x and z directions being
# either both positive or both negative.

p = panda()
mouseControl(p)

x = getX(p.position)
z = getZ(p.position)

# The color of the panda to be different when the x and z coordinates
# are both bigger than 0, or when both are less than 0.

p.color = choose(((x > 0) & (z > 0)) | ((x < 0) & (z < 0)), green, yellow)

start()