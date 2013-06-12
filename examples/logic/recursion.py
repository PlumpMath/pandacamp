from Panda import *

# Simple recursion (counting)
# This function is recursive beacuse note that in the function
# makes a call to the function within the function.  The number parameter
# tells the function to finish recursing after the number < 0.

camera.position = p3(0, -20, 0)  # Stand back to see the herd of pandas!

# This function puts a line of panda
#   The parameter "number" which tells you how many more panda to make
#   The parameter "place" which tells you where the last panda was placed

def pandaLine(number, place):
    # The "if" is to determine whether more pandas are needed.
    if number > 0:
        panda(position = p3 (place, time*7, place),size=1+time/8,)
        panda(position = p3 (place, time*7, -place),size=1+time/8)
        panda(position = p3 (0, time*7, place),size=1+time/8)
        panda(position = p3 (place, time*7, 0),size=1+time/8)

        # Recursive step.  Note that the number must decrease in order to avoid
        # infinite loops.

        pandaLine(number-1, place+2)




pandaLine(100, -100)


start()