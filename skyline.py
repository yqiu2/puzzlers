# the perimeter is the sum of all visible heights and all visible widths
# the width of the skyline is exactly the distance between the rightmost point and the leftmost point minus any ground distances
# to calculate visible heights:
# rather than calculating heights of all buildings and then subtracting hidden heights, since the perimeter at any point can either be flat or vertical,
# the height at any one point is the difference between the max height of points just to the left and right of it.

# from buildings produces list of all start and end points (as doubles) sorted in increasing order with no repeats
def makePointList(buildings):
	points = []
	for building in buildings: 
		# insertion can be optimized by using a insertion sort
		if building[0] not in points:
			points.append(building[0])
		if building[2] not in points:
			points.append(building[2])
	return sorted(points)

# make list of midpoints between the points
def makeMidpointsList(points):
	midpoints = [] # length of midpoints list will be one less than length of points list
	for x in range(0, len(points)-1):
		midpoints.append( float(points[x+1] + points[x])/2.0 )
	return midpoints

# finds the maximum height at a certain point
def maxHeightAt(x, buildings):
	maxHeight = 0
	for building in buildings: 
		# some efficiencies can still be coded in in order to not loop through buildings that obviously can't exist at a certain x
		if (building[0]<x) and (x<building[2]):
			height = building[1]
			if height > maxHeight:
				maxHeight = height
	return maxHeight

# find max height for all points in the midpoints list additionally this list will begin and end with a height of 0 
def makeMidpointsHeightsList(midpoints, buildings):
	midpointHeights = []  # length of this list will be 2 more than midpoints list and 1 more than points list
	midpointHeights.append(0)
	for midpoint in midpoints: 
		midpointHeights.append(maxHeightAt(midpoint,buildings))
	midpointHeights.append(0)
	return midpointHeights

# add visible heights and subtract invisible ground widths
# point[x] is between midpoint[x] and midpoint [x+1]
def add_heights_sub_widths(perimeter, points, midpointsHeights):
	perimeter = perimeter
	for x in range (len(midpointsHeights)-1):
		# add visible heights
		visibleHeight = abs(midpointsHeights[x] - midpointsHeights[x+1])
		print "height change at point {}: {} \t add visibleHeight {}".format(points[x], midpointsHeights[x+1] - midpointsHeights[x], visibleHeight) 
		perimeter += visibleHeight
		# subtract widths that are on the ground
		if x > 0 and midpointsHeights[x] == 0:
			perimeter - (points[x]-points[x-1])
			print "ground level between point {} and {}: subtract {} ".format(points[x-1],points[x], points[x-1]-points[x])
	return perimeter


if __name__ == "__main__":
	buildings = ( (1, 11, 5),(2, 6, 7),(3, 13, 9),(12, 7, 16),(14, 3, 25),(19, 18, 22),(23, 13, 29),(24, 4, 28) )
	points = []
	points = makePointList(buildings)
	print "points :   {}".format(points)
	perimeter = points[len(points)-1] - points[0]
	print "horizontal span: {}".format(perimeter) 
	midpoints = []
	midpoints = makeMidpointsList(points)
	print "midpoints : {}".format(midpoints)
	midpointsHeihts = []
	midpointsHeights = makeMidpointsHeightsList(midpoints, buildings)
	print "mid heights: {}".format(midpointsHeights)
	perimeter = add_heights_sub_widths(perimeter, points, midpointsHeights)

	print 
	print "PERIMETER: {}".format(perimeter)