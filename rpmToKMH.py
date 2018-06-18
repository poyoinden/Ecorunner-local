from __future__ import division
import math

def rpmToKMH(rpm, wheelradius):
	if(rpm < 0):
		return 0
	else:
		speed = wheelradius * 2 * math.pi * rpm * 3.6 / 60
		return int(speed)
