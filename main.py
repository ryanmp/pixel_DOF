from PIL import Image
import random

img = Image.open('images/original.jpg')
pixels = img.load() # create the pixel map

def get_avg_color(x, y, size):
	pixel_sum = [0,0,0]

	min_x = max(0,x-size)
	max_x = min(img.size[0],x+size)
	min_y = max(0,y-size)
	max_y = min(img.size[1],y+size)	

	for x in xrange(min_x,max_x):
		for y in xrange(min_y,max_y):
			for c in [0,1,2]:
				pixel_sum[c] += pixels[x,y][c]

	total_pixels = (max_x - min_x) * (max_y - min_y)
	average_pixel = [i/total_pixels for i in pixel_sum]

	return average_pixel



def set_color(c, x, y, size):
	c = tuple(c)
	min_x = max(0,x-size)
	max_x = min(img.size[0],x+size)
	min_y = max(0,y-size)
	max_y = min(img.size[1],y+size)	

	for x in xrange(min_x,max_x):
		for y in xrange(min_y,max_y):
			pixels[x,y] = c


num_passes = 40
for i in xrange(num_passes):

	this_size = random.randrange(10,50)*2
	this_x = random.randrange(0+this_size/2,img.size[0]-this_size/2)
	this_y = random.randrange(0+this_size/2,img.size[1]-this_size/2)

	p = get_avg_color(this_x,this_y,this_size)
	set_color(p,this_x,this_y,this_size)

img.show()
#img.save('test.png')

