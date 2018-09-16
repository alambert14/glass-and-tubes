#!/usr/bin/env python3

class Edge:

	def __init__(self, segments=[]):
		self.segments = segments
	
	def get_list(self):
		return_list = []
		for segment in self.segments:
			return_list.append(segment.get_tuple())
		return return_list
