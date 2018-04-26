from __future__ import division
import math

def rpmToKMH(rpm, wheelradius):
	if(rpm < 0):
		return 0
	else:
		speed = wheelradius * 2 * math.pi * 60/1000 * rpm
		return int(speed)
