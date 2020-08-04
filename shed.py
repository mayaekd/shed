from mayavi import mlab

def plotRectangle():
	# Shed
	x = np.array([[0,25],[0,25],[0,25],[0,25],[0,25],[0,25]])
	y = np.array([[0,0],[10,10],[20,20],[20,20],[0,0],[0,0]])
	z = np.array([[10,10],[15,15],[10,10],[-5,-5],[-5,-5],[10,10]])

	# Box
	# x = np.array([[0,25],[0,25],[0,25],[0,25],[0,25]])
	# y = np.array([[0,0],[20,20],[20,20],[0,0],[0,0]])
	# z = np.array([[10,10],[10,10],[-5,-5],[-5,-5],[10,10]])

	# Two different pitches
	# x = np.array([[0,25],[0,25],[0,25],[0,25],[0,25],[0,25]])
	# y = np.array([[0,0],[10,10],[20,20],[20,20],[0,0],[0,0]])
	# z = np.array([[10,10],[15,10],[10,10],[-5,-5],[-5,-5],[10,10]])

	mesh = mlab.mesh(x, y, z, colormap = "plasma")
	return mesh

if __name__ == "__main__":
	plotRectangle()
	mlab.show()
