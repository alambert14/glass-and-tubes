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
	loop1 = Loop([e1])
	graveyard.append(loop1.get_list())
	previous = loop1

	loopNum = 10

	for f in range(loopNum):
		nodes = []
		print('nodes: ')
		print(nodes)
		edgeList = previous.get_list()
		print('edgeList: ')
		print(edgeList)
		for i in range(len(edgeList)):
			#Can make random later
			seg = edgeList[i][0]
			print('seg')
			print(seg)
			middle = Segment(seg[0], seg[1]).bisection()
			nodes.append(middle)
		print('nodes: ')
		print(nodes)

		###Path
		x1 = randint(0, xWidth)
		y1 = randint(0, yWidth)
		segList = find_path((x1, y1), nodes)
		print("segList:")
		print(segList)

		segInEdge = []
		edgeInLoop = []
		for segment in segList:
			segInEdge.append(segment)
			print("segInEdge")
			print(segInEdge)
			if(check_intersect(segment.get_tuple(), graveyard)):
				print("intersect")
				edgeInLoop.append(segInEdge)
				segInEdge = []


		current = Loop(edgeInLoop)
		print("current:")
		print(current.get_list())
		graveyard.append(previous.get_list())
		previous = current
		print("previous:")
		print(previous.get_list())
	graveyard.append(current.get_list())
	
	####Graohics
	#maxThickness = 50
	#outlineThicknessRatio = 5
	#loopNum = randint(1, 100)

	frame = 0
	for loop in graveyard:
		frame+=1
		print(frame)
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
				#curve.setFill(color_rgb(int(frame*(255/(loopNum+int(loopNum/10)))), 0, 255-int(frame*(255/(loopNum+int(loopNum/10))))))
				curve.setFill(color_rgb(randint(0,255), randint(0,255),randint(0,255)))
				curve.draw(win)
				time.sleep(1)
				win.flush()
		#win.getMouse()
		#time.sleep(0.5)
		#for item in win.items[:]:
		#	item.undraw()

	print("Done")

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