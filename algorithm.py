#!/usr/bin/env python3

from random import randint

n = 0
max_n = 5

current_loop = []
last_loop = []
graveyard=[]

h = 512
w = 512
init_sq_size = 128
while(n < 100):
	#if it is the first iteration, just make one loop in a random position (initialize the lists)

	#L1 graveyard (what will be printed in the end): Store all of the loops(segments((x,y),(x,y)))
	#L2 just the last loop: [edges[segments(p1,p2)]]
	#L3 current loop: [edges[segments(p1,p2)]]

	if n==0:
		current_loop = Loop()
		current_loop.edges.append(Edge())
		current_loop.edges[0].segments.append(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #top
		current_loop.edges[0].segments.append(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2-init_sq_size/2),(h/2+init_sq_size/2)))) #left
		current_loop.edges[0].segments.append(Segment(((w/2-init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2+init_sq_size/2)))) #bottom
		current_loop.edges[0].segments.append(Segment(((w/2+init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #right
		last_loop = current_loop
		graveyard.append(current_loop)

	else:

		#pick an edge and find the middle of it
		crossed_segment = last_loop[0][0]
		horizontal = True
		#if x values are the different then true, if x values are the same then false
		if crossed_segment[0][0] == crossed_segment[1][0]:
			horizontal = False
		
		bisect = 0
		if horizontal:
			bisect = ((crossed_segment[0][0]+crossed_segment[1][0])/2),crossed_segment[0][1])
			segment  = find_path(bisect,last_loop)
			#path is a list of segments

		else:
			bisect = ((crossed_segment[0][1]+crossed_segment[1][1])/2),crossed_segment[0][0])




 	           
