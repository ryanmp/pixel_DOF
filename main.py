from PIL import Image
import random, datetime

img = Image.open('images/original.jpg')
img_pixels = img.load()

dof_map = Image.open('images/gradient2.jpg').load()
 
class V: # vector
    def __init__(self, x, y):
        self.x = x  
        self.y = y      


def get_avg_color(x, y, size):
	pixel_sum = [0,0,0]

	min_x = max(0,x-size)
	max_x = min(img.size[0],x+size)
	min_y = max(0,y-size)
	max_y = min(img.size[1],y+size)	

	for x in xrange(min_x,max_x):
		for y in xrange(min_y,max_y):
			for c in [0,1,2]:
				pixel_sum[c] += img_pixels[x,y][c]

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
			img_pixels[x,y] = c


def random_sampling(num_samples):
	for i in xrange(num_samples):

		sample_loc = V(random.randrange(0,img.size[0]),random.randrange(0,img.size[1]))

		max_size = 100
		this_size = (((dof_map[sample_loc.x,sample_loc.y])/255.0) * max_size) + 1
		this_size = int(this_size)
		
		p = get_avg_color(sample_loc.x,sample_loc.y,this_size)
		set_color(p,sample_loc.x,sample_loc.y,this_size)

def grid_sampling(res):
	for x in xrange(0,img.size[0],res):
		for y in xrange(0,img.size[1],res):

			sample_loc = V(x,y)

			max_size = 100
			this_size = (((dof_map[sample_loc.x,sample_loc.y])/255.0) * max_size) + 1
			this_size = int(this_size)
			
			p = get_avg_color(sample_loc.x,sample_loc.y,this_size)
			set_color(p,sample_loc.x,sample_loc.y,this_size)



#random_sampling(5000) # first method of creating image
#grid_sampling(40)

img.show()
st = datetime.datetime.now().strftime('%Y%m%d_%H_%M_%S')
img.save('test_out_'+st+'.png')


