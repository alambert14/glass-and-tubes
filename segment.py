#!/usr/bin/env python3

class Segment:

	#two points, tuples
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def horizontal(self):
		if p1[0] == p2[0]:
			return False
		else:
			return True

	#returns point where the segment is bisected
	def bisection(self):
		if self.horizontal():
			return ((self.p1[0]+self.p2[0])/2,self.p1[1])
	
	def getTuple(self):
		return (p1,p2)


