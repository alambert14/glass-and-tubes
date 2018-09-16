#!/usr/bin/env python3

class Loop:

	#list of edges
	def __init__(self, edges=[]):
		self.edges = edges
			
	def get_list(self):
		return_list = []
<<<<<<< HEAD
		for edge in self.edges:
=======
		for edge in edges:
>>>>>>> acdf585b0c17a879537fd4775996823efd094f5d
			return_list.append(edge.get_list())
		return return_list
