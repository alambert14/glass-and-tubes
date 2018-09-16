#!/usr/bin/env python3

class Edge:

	def __init__(self, segments=[]):
		self.segments = segments
	
	def get_list(self):
		return_list = []
		for segment in segments:
			return_list.append(segment.get_list)
		return return_list
