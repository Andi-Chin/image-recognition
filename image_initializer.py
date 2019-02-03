
from PIL import Image

def initialize(imageName, iterations):
	im = Image.open(imageName) # Can be many different formats.
	pix = im.load()

	width, height = im.size


	def initialize_quadrant_1():
		iterations = 0
		r, g, b = (0, 0, 0)
		for x in range(round(width / 2)):
			for y in range(round(height / 2)):
				R, G, B, A = pix[x, y]
				r += R
				g += G
				b += B
				iterations += 1
		r, g, b = (r / iterations, g / iterations, b / iterations)

		for x in range(round(width / 2)):
			for y in range(round(height / 2)):
				pix[x, y] = round(r), round(g), round(b)
		return r, g, b
	def initialize_quadrant_2():
		iterations = 0
		r, g, b = (0, 0, 0)
		for x in range(round(width / 2), width):
			for y in range(round(height / 2)):
				R, G, B, A = pix[x, y]
				r += R
				g += G
				b += B
				iterations += 1
		r, g, b = (r / iterations, g / iterations, b / iterations)

		for x in range(round(width / 2), width):
			for y in range(round(height / 2)):
				pix[x, y] = round(r), round(g), round(b)

		return r, g, b
	def initialize_quadrant_3():
		iterations = 0
		r, g, b = (0, 0, 0)
		for x in range(round(width / 2)):
			for y in range(round(height / 2), height):
				R, G, B, A = pix[x, y]
				r += R
				g += G
				b += B
				iterations += 1
		r, g, b = (r / iterations, g / iterations, b / iterations)

		for x in range(round(width / 2)):
			for y in range(round(height / 2), height):
				pix[x, y] = round(r), round(g), round(b)

		return r, g, b
	def initialize_quadrant_4():
		iterations = 0
		r, g, b = (0, 0, 0)
		for x in range(round(width / 2), width):
			for y in range(round(height / 2), height):
				R, G, B, A = pix[x, y]
				r += R
				g += G
				b += B
				iterations += 1
		r, g, b = (r / iterations, g / iterations, b / iterations)

		for x in range(round(width / 2), width):
			for y in range(round(height / 2), height):
				pix[x, y] = round(r), round(g), round(b)

		return r, g, b

	initialize_quadrant_1()
	initialize_quadrant_2()
	initialize_quadrant_3()
	initialize_quadrant_4()

	im.save('resultData/imageName%s.png' % (iterations))

for i in range(20):
	try:
		initialize('patrickStarData/patrick' + str(i), i)
	except:
		pass


