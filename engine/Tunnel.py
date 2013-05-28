## Tunnel creation
## TO-DO:
## * Integrate P3() and HPR()

import g 
from panda3d.core import Fog
from direct.showbase.DirectObject import DirectObject
from Time import *
from Color import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from Handle import *
from math import pi, cos, sin
import os
import sys
###! Probably don't need all of these !
###! Confirm ASAP !

class Tunnel():

	#Init function for creating the models, fog, and attaching to the timer.
	#Currently, some are temporary before I deduce the needed default.
	def __init__(self, name = "tunnel", fogName = "distanceFog", axis = "Y", direction = "+", scale = 1.0, tunnelTime = 2, positionX = 0, positionY = 0, positionZ = 0, fogIntensity = .8, fogColorR = 255, fogColorG = 255, fogColorB = 255, tunnelImage="tunnel/tunnel.png", tunnelModel="tunnel/tunnel", numSegments="4", relTunnelLength="50", segScale1=".155", segScale2=".155", segscale3=".305"):
		if direction == "-":
			direction = -1
		elif direction == "+":
			direction = 1
		else:
			print "Unknown direction. Assuming negative."
			direction = -1
		#First, set the fog.
		self.fog = Fog(fogName)
		#color it.
		self.fog.setColor=Color(r = fogColorR, g = fogColorG, b = fogColorB)
		#Intensity.
		self.fog.setExpDensity=(fogIntensity)
		#And parent it to the render.
		#Fog is needed so hat you can't see the tunnel end.
		render.setFog(self.fog)

		#Copypasted from tutorial and modified.
    		#Creates the list [None, None, None, None]
		##As far as I can tell, this is used to loop the tunnels and easily reference all 4.
    		self.tunnel = [None for i in range(numSegments)]
		##Texture it.
		tex = loader.loadTexture(findTexture(tunnelImage))

    		for x in range(numSegments):
      			#Load a copy of the tunnel
      			self.tunnel[x] = loader.loadModel(tunnelModel)
         		selftunnel[x].setTexture(tex, 1)
			##Changeme, need to figure out how to retexture
     			#The front segment needs to be attached to render
			##So it actually gets rendered.
     			if x == 0: self.tunnel[x].reparentTo(render)
     			#The rest of the segments parent to the previous one, so that by moving
     			#the front segement, the entire tunnel is moved
			##For easy chaining.
     			else:   self.tunnel[x].reparentTo(self.tunnel[x-1])
   			#We have to offset each segment by its length so that they stack onto
    			#each other. Otherwise, they would all occupy the same space.
			###! Check these values!
			if axis == "Z":
				self.tunnel[x].setHPR(0,0,0)
				self.tunnel[x].setPos(0, 0, direction*relTunnelLength)
			elif axis == "Y":
				self.tunnel[x].setHPR(-pi,0,0)
				self.tunnel[x].setPos(0, direction*relTunnelLength, 0)
			elif axis == "X":
				self.tunnel[x].setHPR(pi,0,0)
				self.tunnel[x].setPos(direction*relTunnelLength, 0, 0)
			else:
				print "Invalid direction. Not uppercase?"
				print "Defaulting to Y"
				self.tunnel[x].setHPR(-pi,0,0)
		self.contTunnel()

	def contTunnel(self):
		#This line uses slices to take the front of the list and put it on the
   		#back. For more information on slices check the Python manual
    		self.tunnel = self.tunnel[1:]+ self.tunnel[0:1]
    		#Set the front segment (which was at TUNNEL_SEGMENT_LENGTH) to 0, which
    		#is where the previous segment started
    		self.tunnel[0].setZ(positionZ)
   		#Reparent the front to render to preserve the hierarchy outlined above
    		self.tunnel[0].reparentTo(render)
    		#Set the scale to be apropriate (since attributes like scale are
    		#inherited, the rest of the segments have a scale of 1)
    		self.tunnel[0].setScale(segScale1, segScale2, segScale3)
    		#Set the new back to the values that the rest of teh segments have
    		self.tunnel[numSegments-1].reparentTo(self.tunnel[2])
    		self.tunnel[numSegments-1].setZ(direction*relTunnelLength)
    		self.tunnel[numSegments-1].setScale(scale)
    	
    		#Set up the tunnel to move one segment and then call contTunnel again
    		#to make the tunnel move infinitely
    		self.tunnelMove = Sequence(
			LerpFunc(self.tunnel[0].setZ,
				duration = tunnelTime,
				fromData = 0,
				toData = relTunnelLength*((1/numSegments)+.05)),
			Func(self.contTunnel)
		)
		self.tunnelMove.start()
