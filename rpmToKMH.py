from __future__ import division
import math

def rpmToKMH(rpm):
	wheelCirc = 0.235 * 2 * math.pi
	rps = int(rpm) / 60
	speed = rps * wheelCirc * 3.6
	speedToWrite = 1200 + int(round(speed))%100
	
	return speedToWrite
