#!/usr/bin/env python3

from random import randint
from graphics import *
from loop import *
from edge import *
from segment import *
from grid import *



#input:
#starting point, list of nodes to hit
#output:
#a new loop
def find_path(start_pt, nodes):
	list_of_segments = []
	list_of_edges = []
	current_pt = start_pt
	for node in nodes:
		new_edge = Edge()
		new_edge.add_segment(Segment(current_pt,(current_pt[0],node[1])))
		new_edge.add_segment(Segment((current_pt[0],node[1]), node))
		current_pt = node
		list_of_edges.append(new_edge)
	list_of_edges[0].add_segment(Segment(current_pt,(current_pt[0],start_pt[1])))
	list_of_edges[0].add_segment(Segment((current_pt[0],start_pt[1]), start_pt))
	return_loop = Loop()
	return_loop.egdes = list_of_edges
	return return_loop

def draw_segments(segs):
	####Graohics
	maxThickness = 50
	outlineThicknessRatio = 5
	#loopNum = randint(1, 100)
	loopEdges = 7

	frame = 0
	for loop in graveyard:
		frame+=1
		for edge in loop:
			for drawSeg in edge:
				#thickness = maxThickness-int(frame*(maxThickness/loopNum))
				thickness = 10
				
				x1 = drawSeg[0][0]
				y1 = drawSeg[0][1]
				x2 = drawSeg[1][0]
				y2 = drawSeg[1][1]
				if(x1 == x2):
					if(y1 > y2):
						y2+=thickness/2
						y1-=thickness/2
					else:
						y1+=thickness/2
						y2+=thickness/2
				else:
					if(x1>x2):
						x1+=thickness/2
						x2-=thickness/2
					else:
						x1-=thickness/2
						x2+=thickness/2
				curve = Line(Point(x1, y1), Point(x2, y2))
				#thickness = int(frame*(maxThickness/loopNum))
				curve.setWidth(thickness)
				#curve.setFill(color_rgb(int(frame*(255/loopNum)), 0, 255-int(frame*(255/(2*loopNum)))))
				curve.setFill(color_rgb(int(frame*(255/(loopNum+int(loopNum/10)))), 0, 255-int(frame*(255/(loopNum+int(loopNum/10))))))
				curve.draw(win)
				time.sleep(1)
				win.flush()


n = 0
max_n = 5

current_loop = None
last_loop = None
graveyard = []

h = 512
w = 512
init_sq_size = 128
while(n < 100):
	#if it is the first iteration, just make one loop in a random position (initialize the lists)

	#L1 graveyard (what will be printed in the end): Store all of the segments((x,y),(x,y)))
	#L2 just the last loop: [edges[segments(p1,p2)]]
	#L3 current loop: [edges[segments(p1,p2)]]

	if n == 0:
		current_loop = Loop()
		current_loop.add_edge(Edge())
		current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #top
		current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2-init_sq_size/2),(h/2+init_sq_size/2)))) #left
		current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2+init_sq_size/2)))) #bottom
		current_loop.edges[0].add_segment(Segment(((w/2+init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #right
		last_loop = current_loop

		graveyard.append()

	else:
		#a list of points
		nodes = []
		for edge in last_loop.edges:
			nodes.append(edge.segments[0].bisection())
		
		current_loop = find_path((randint(0,w),randint(0,h)),nodes)
		
		for edge in last_loop.edges:
			for seg in edge.segments:
				graveyard.append(seg)
		last_loop = current_loop
		
	n += 1






 			   
