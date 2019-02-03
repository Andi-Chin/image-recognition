from random import randint as rd
class Quadrant():


	w1 = rd(-100, 100) / 100
	w2 = rd(-100, 100) / 100
	w3 = rd(-100, 100) / 100
	w4 = rd(-100, 100) / 100

	b1 = rd(-100, 100) / 100
	b2 = rd(-100, 100) / 100
	b3 = rd(-100, 100) / 100
	b4 = rd(-100, 100) / 100


	def __init__(self): #has to open image with PIL*********************
		self.w = rd(-100, 100) / 100
		self.b = rd(-100, 100) / 100
		self.rgb = None


	def initialize(self, num):
		if num == 1:
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

			self.rgb = initialize_quadrant_1()

		elif num == 2:

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
				return r, g, b

			self.rgb = initialize_quadrant_2()
		elif num == 3:
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

				return r, g, b

			self.rgb = initialize_quadrant_3()

		elif num == 4:
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

				return r, g, b

			self.rgb = initialize_quadrant_4()

