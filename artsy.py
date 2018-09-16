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
	graveyard.append(loop1)
	previous = loop1

	nodes = []
	edgeList = previous.get_list()
	for i in range(len(edgeList)):
		#Can make random later
		seg = edgeList[i][0]
		middle = Segment(seg[0], seg[1]).bisection()
		nodes.append(middle)

	###Path





	###
	x1 = randint(0, xWidth)
	y1 = randint(0, yWidth)

	maxThickness = randint(1, 50)
	outlineThicknessRatio = randint(0, 50)
	loopNum = randint(1, 100)
	loopEdges = randint(1,20)

	for frame in range(loopNum):
		pointList = []
		pointList.append([randint(0, xWidth), randint(0, yWidth)])
		direction = 0
		for i in range(loopEdges):
			if(randint(0,1)==0):
				x = pointList[-1][0]
				y = randint(0, yWidth)
				direction = 0
			else:
				x = randint(0, xWidth)
				y = pointList[-1][1]
				direction = 1
			pointList.append([x,y])
		if(direction == 0):
			x = pointList[0][0]
			y = pointList[-1][1]
			pointList.append([x,y])
		else:
			x = pointList[-1][0]
			y = pointList[0][1]
			pointList.append([x,y])
		pointList.append(pointList[0])

		for i in range(len(pointList)-1):
			#thickness = maxThickness-int(frame*(maxThickness/loopNum))
			thickness = int(frame*(maxThickness/loopNum))
			outlineThickness = thickness*(1+outlineThicknessRatio/100)
			###Draw outline curve first
			x1 = pointList[i][0]
			y1 = pointList[i][1]
			x2 = pointList[i+1][0]
			y2 = pointList[i+1][1]
			if(x1 == x2):
				if(y1 > y2):
					y2+=outlineThickness/2
					y1-=outlineThickness/2
				else:
					y1+=outlineThickness/2
					y2+=outlineThickness/2
			else:
				if(x1>x2):
					x1+=outlineThickness/2
					x2-=outlineThickness/2
				else:
					x1-=outlineThickness/2
					x2+=outlineThickness/2
			curveOutline = Line(Point(x1, y1), Point(x2, y2))
			curveOutline.setWidth(outlineThickness)
			curveOutline.setFill('white')
			curveOutline.draw(win)

		for i in range(len(pointList)-1):
			x1 = pointList[i][0]
			y1 = pointList[i][1]
			x2 = pointList[i+1][0]
			y2 = pointList[i+1][1]
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
			#thickness = maxThickness-int(frame*(maxThickness/loopNum))
			thickness = int(frame*(maxThickness/loopNum))
			curve.setWidth(thickness)
			#curve.setFill(color_rgb(int(frame*(255/loopNum)), 0, 255-int(frame*(255/(2*loopNum)))))
			curve.setFill(color_rgb(int(frame*(255/(loopNum+int(loopNum/10)))), 0, 255-int(frame*(255/(loopNum+int(loopNum/10))))))
			curve.draw(win)
	win.flush()
	#win.getMouse()
	time.sleep(0.5)
	for item in win.items[:]:
		item.undraw()

	win.getMouse()
	win.close()

main()