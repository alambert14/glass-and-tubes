#!/usr/bin/env python3

class Loop:

	#list of edges
	def __init__(self, edges=[]):
		self.edges = edges
			
	def get_list(self):
		return_list = []
		for edge in self.edges:
			return_list.append(edge.get_list())
		return return_list
