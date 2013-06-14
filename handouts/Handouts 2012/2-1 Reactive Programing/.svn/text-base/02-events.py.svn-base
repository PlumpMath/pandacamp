from Panda import *



p = panda()
grassScene()

# An event is something that "happens" as the program runs, like a button press or mouse click.
# Events can carry values - a message that comes when the event happens
# Here are some events you can use:
#    lbp, rbp, rbr, lbr: mouse presses / releases - give these a value with tag: tag(value, lbp)
#    key("name", value)
#    keyUp("name", value)
#    timeIs(t, value)
#  Special key names: "escape", "f"+"1-12" (e.g. "f1","f2",..."f12"), "scroll_lock"
#  "backspace", "insert", "home", "page_up", "num_lock"
#  "tab",  "delete", "end", "page_down"
#  "caps_lock", "enter", "arrow_left", "arrow_up", "arrow_down", "arrow_right"
#  "shift", "lshift", "rshift",
#  "control", "alt", "lcontrol", "lalt", "space", "ralt", "rcontrol"

# Use + to combine events
# Use hold to remember the most recent value associated with an event: hold(initialValue, event)

# For example, this sets the size of the panda using the arrow keys, the position using the mouse buttons, and changes the color at
# the given times.

p.size = hold(1, key('arrow_up', .5) + key('arrow_down', 1.5))
p.position = hold(P3(0,0,0), tag(P3(0,0,1), lbp) + tag(P3(0,0,-1), rbp))
p.color = hold(red, timeIs(2, green) + timeIs(4, white))

# Write a panda controller that moves the panda to a 4 different locations using 4 different events

# Next, use the same technique to write a velocity controller that responds to the arrow keys and the space bar (to stop).

# Try the same thing to make the panda move left and right using the mouse - move left or right using the left / right buttons
# and stop when the button is released

# Add a timer to make the panda stop after 10 seconds



start()