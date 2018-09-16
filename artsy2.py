from graphics import *
from random import randint
import time
from loop import *
from edge import *
from segment import *

def main():
	xWidth = 1920
	yWidth = 1080
	win = GraphWin('Curves', xWidth, yWidth) # give title and dimensions
	win.setBackground('white')
	win.autoflush = False		  # NEW: set before animation
	
	graveyard = []
	previous = Loop()
	current = Loop()

	###Generate first loop
	#Add to Graveyard
	#Add to Previous

	###For each next loops:
	# For each edge in previous loop
	# Pick random segment
	# Pick point along segment(Nodes)
	# Start in random position
	# Path to first node
	# Path to next node
	# Repeat
	# Path to original point
	# Check each segment in L3 for intersects in Graveyard
	# Use to mark edges
	# Mark random point on an edge as nodes for next loop




	###Create First Loop
	x1 = randint(0, xWidth)
	y1 = randint(0, yWidth)
	x2 = x1
	y2 = randint(0, xWidth)
	x3 = randint(0, yWidth)
	y3 = y2
	x4 = x3
	y4 = randint(0, xWidth)
	s1 = Segment((x1, y1), (x2, y2))
	s2 = Segment((x2, y2), (x3, y3))
	s3 = Segment((x3, y3), (x4, y4))
	s4 = Segment((x4, y4), (x1, y2))
	e1 = Edge([s1, s2, s3, s4])

	h = yWidth
	w = xWidth
	init_sq_size = 512
	current_loop = Loop()
	current_loop.add_edge(Edge())
	current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #top
	current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2-init_sq_size/2)),((w/2-init_sq_size/2),(h/2+init_sq_size/2)))) #left
	current_loop.edges[0].add_segment(Segment(((w/2-init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2+init_sq_size/2)))) #bottom
	current_loop.edges[0].add_segment(Segment(((w/2+init_sq_size/2),(h/2+init_sq_size/2)),((w/2+init_sq_size/2),(h/2-init_sq_size/2)))) #right
	graveyard.append(current_loop)
	previous = current_loop

	loopNum = 4

	for f in range(loopNum):
		nodes = []
		edgeList = previous.edges
		print('edgeList: ')
		print(edgeList)
		for edge in edgeList:
			#Can make random later
			if len(edge.segments) > 0:
				seg = edge.segments[0]
			else:
				seg = Segment((0,0), (10,10))
			print('seg')
			print(seg)
			middle = seg.bisection()
			nodes.append(middle)
		print('nodes: ')
		print(nodes)

		###Pathnodes = []
		x1 = randint(0, xWidth)
		y1 = randint(0, yWidth)
		segList = find_path((x1, y1), nodes)
		print("segList:")
		print(segList)

		segInEdge = []
		edgesInLoop = []
		for segment in segList:
			segInEdge.append(segment)
			print("segInEdge")
			print(segInEdge)
			print("edgeInLoop")
			print(edgesInLoop)

			for loop in graveyard:
				for edge in loop.edges:
					for graveSeg in edge.segments:
						if(segment.intersects(graveSeg)):
							edgesInLoop.append(Edge(segInEdge))
							segInEdge = []

		current = Loop(edgesInLoop)
		print("current:")
		graveyard.append(previous)
		previous = current
		print("previous:")
		print(previous.get_list())
	graveyard.append(current)
	
	####Graohics
	maxThickness = 20
	minThickness = 10
	#outlineThicknessRatio = 5
	#loopNum = randint(1, 100)

	frame = 0
	total = len(graveyard)
	for loop in graveyard:
		frame+=1
		print(frame)
		length = len(loop.edges)
		for edge in loop.edges:
			for drawSeg in edge.segments:
				#thickness = maxThickness-int(frame*(maxThickness/loopNum))
				#thickness = int(frame*(maxThickness/total))
				thickness = maxThickness-int(frame*(maxThickness/total))+minThickness
				
				x1 = drawSeg.p1[0]
				y1 = drawSeg.p1[1]
				x2 = drawSeg.p2[0]
				y2 = drawSeg.p2[1]
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
				#thickness = int(frame*(maxThickness/total))
				curve.setWidth(thickness)
				red = int(frame*(255/loopNum))
				blue = 255-int(frame*(255/(loopNum)))
				if(red < 0):
					red = 0
				if(red > 255):
					red = 255
				if(blue < 0):
					blue = 0
				if(blue > 255):
					blue = 255
				#curve.setFill(color_rgb(red, 0, blue))
				#curve.setFill('red')
				curve.setFill(color_rgb(int(frame*(255/(total+int(total/10)))), 0, 255-int(frame*(255/(total+int(total/10))))))
				#curve.setFill(color_rgb(randint(0,255), randint(0,255),randint(0,255)))
				curve.draw(win)
				win.flush()
			#time.sleep(1)
		#win.getMouse()
		time.sleep(0.5)
		#for item in win.items[:]:
		#	item.undraw()

	print("Done")
	time.sleep(1000)
	win.getMouse()
	win.close()

#input:
#starting point, list of nodes to hit
#output:
#list of segments (or new edges)
def find_path(start_pt, nodes):
	list_of_segments = []
	current_pt = start_pt
	for node in nodes:
		list_of_segments.append(Segment(current_pt,(current_pt[0],node[1])))
		list_of_segments.append(Segment((current_pt[0],node[1]), node))
		current_pt = node
	list_of_segments.append(Segment(current_pt,(current_pt[0],start_pt[1])))
	list_of_segments.append(Segment((current_pt[0],start_pt[1]), start_pt))
	return list_of_segments

def check_intersect(segment, graveyard):
	if(segment[0][0] == segment[1][0]):
		segmentHoriz = True
	else:
		segmentHoriz = False
	for loop in graveyard:
		for edge in loop:
			for graveSeg in edge:
				if(graveSeg[0][0] == graveSeg[1][0]):
					graveSegHoriz = True
				else:
					graveSegHoriz = False
				if(segmentHoriz and not graveSegHoriz):
					if((segment[0][1] <= graveSeg[0][1] and segment[0][1] >= graveSeg[1][1]) or (segment[0][1] >= graveSeg[0][1] and segment[0][1] <= graveSeg[1][1])):
						if((graveSeg[0][0] <= segment[0][0] and graveSeg[0][0] >= segment[1][0]) or (graveSeg[0][0] >= segment[0][0] and graveSeg[0][0] <= segment[1][0])):
							return True
				if(not segmentHoriz and graveSegHoriz):
					if((segment[0][0] <= graveSeg[0][0] and segment[0][0] >= graveSeg[1][0]) or (segment[0][0] >= graveSeg[0][0] and segment[0][0] <= graveSeg[1][0])):
						if((graveSeg[0][1] <= segment[0][1] and graveSeg[0][1] >= segment[1][1]) or (graveSeg[0][1] >= segment[0][1] and graveSeg[0][1] <= segment[1][1])):
							return True
	print("No Intersect")
	return False



main()
