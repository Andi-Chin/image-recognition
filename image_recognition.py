from PIL import Image
import math
from random import randint as rd
from image_initializer import initialize

def classify(rgb, w, b):
	def sigmoid(x):
		return 1 / (1 + (math.e ** -x))

	r, g, b = rgb

	r = sigmoid(r * w + b)
	g = sigmoid(g * w + b)
	b = sigmoid(b * w + b)

	return sum([r, g, b]) / 3


w1 = rd(-100, 100) / 100
w2 = rd(-100, 100) / 100
w3 = rd(-100, 100) / 100
w4 = rd(-100, 100) / 100

b1 = rd(-100, 100) / 100
b2 = rd(-100, 100) / 100
b3 = rd(-100, 100) / 100
b4 = rd(-100, 100) / 100


#@param: average rgb color of the quadrate
def result(quad1, quad2, quad3, quad4):
	quad1 = classify(quad1, w1, b1)
	quad2 = classify(quad2, w2, b2)
	quad3 = classify(quad3, w3, b3)
	quad4 = classify(quad4, w4, b4)

	return sum([quad1, quad2, quad3, quad4]) / 4


quad1, quad2, quad3, quad4 = initialize()

print(w1, w2, w3)
print(b1, b2, b3)

print()
print(result(quad1, quad2, quad3, quad4))

def generation(gene):
	