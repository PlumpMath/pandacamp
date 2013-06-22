from Panda import *


#Particle effects are created much like Models.
#Simply call the function with the name of the particle effect
world.color = black

#Run each of these and see what they do
intervalRings(position = p3(-1,0,0), size = .15)
#likeFountainWater(position = p3(0,0,0), size = .25)
shakenSparkles(position = p3(2,0,0), size = .25)
warpSpeed(position = p3(-2,0,2), size = .015)
heavySnow(position = p3(1,0,-1), size = .05)
lightSnow(position = p3(1,0,1), size =.05)
#explosions(position = p3(0,0,-2), size = .25)
fireWork(position = p3(-1,0,-1), size = .25)
fireWorks(position = p3(-2,0,0), size = .25)
explosion(position = p3(-1,0,0), size = .25 )
warpFace(position = p3(0,0,1), texture="face.jpg")
fireish(position = p3(0,0,0), size = .25)



# You can give these effects a duration - just add duration = n, where n is in seconds

# You can set the position of an effect (or any other model) based on the position of
# another model.  Make a panda that moves left and right using the arrow keys.  Set him
# on fire by positioning a fireish at the same place (or better just a little higher)

# Instead of having the panda on fire all the time, start the fire when you hit a space.
# Make the fire die out after 2 seconds.  See if you can make it get smaller as it dies out - use localTime to do this.
# localTime is like time except that it starts at 0 when the model is created, not at the start of the program

start()