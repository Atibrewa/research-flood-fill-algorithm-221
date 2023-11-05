from drawLine import *
import sys
sys.setrecursionlimit(2*10**8)
from graphics import *
'''
100 100
50 0
100 -100
0 -50
-100 -100
-50 0
-100 100
0 50
'''
def boundaryFill(pixel, stack, filled, win, fillColor):
	while(stack != []):		
		x, y = stack.pop()
		if((x, y) not in pixel and (x, y) not in filled):
			win.plot(x, y, fillColor)
			stack += [(x+1, y),(x, y+1),(x, y-1),(x-1, y)]
			filled.append((x, y))

def main():
	vert = []
	
	while(1):
		try:
			x, y=map(int, input('Next vert?').split())
			vert.append((x, y))
		except:
			print(vert)
			break
	if(input('Defualt viewPort is (-400 -400, 400 400). Change?(y/Y)') in ('y', 'Y')):
		x , y = map(int, input('viewPort\'s xMax yMax : ').split())
		new_view = ViewPort(-x, -y, x, y)
	else:
		new_view = ViewPort(-400, -400, 400, 400)	
	print('ViewPort :', new_view)
	
	pixel = []
	filled = []
	pixel_dict = {}
	vert += [vert[0]]
	win = new_view.init_view()
	
	for i in range(len(vert)-1):
		pixel += bresenham(*vert[i], *vert[i+1])

	for i in pixel:
		x, y = i
		win.plot(*i)
		pixel_dict[(x, y)] =1
	point = win.getMouse()
	stack = [(int(point.getX()), int(point.getY()))]	
	
	#Comment this line for just polygon
	start_time = time.time()
	boundaryFill(pixel_dict,stack,filled,win, 'blue')
	end_time = time.time()
	print("time: ", end_time - start_time)


	input('Exit')	
if __name__=='__main__':
	main()