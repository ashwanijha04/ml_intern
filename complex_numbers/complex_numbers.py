import math


class Complex:
	x = 0.0
	y = 0.0

	# Creating the class constructor
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "({0} + {1}i)".format(self.x,self.y)

	# Returns the real part of the number
	def real(self):
		return self.x

	# Returns the imaginary part of the number
	def imag(self):
		return self.y

	# Returns the argument
	def argument(self):
		try:
			return math.atan(self.y/self.x)
		except ZeroDivisionError:
			return math.pi/2

	def conjugate(self):
		return "({0} - {1}i)".format(self.x,self.y)

	def __add__(self,other):
		x = self.x + other.x
		y = self.y + other.y
		return Complex(x, y)

	def __sub__(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return Complex(x, y)

	def __mul__(self, other):

		"""
		(x1+iy1)*(x2+iy2) 
		= (x1x2 - y1y2) + i(x1y2 + y1x2)

		"""
		x = (self.x)*(other.x) - (self.y)*(other.y)
		y = (self.x)*(other.y) + (self.y)*(other.x)
		return Complex(x, y)

	def __truediv__(self, other):

	"""
	(x1 + iy1)/(x2 + iy2)
	= ((x1x2 + y1y2) - i(x1y2 - x2y1))/(x2^2 - y2^2)

	"""
		x = ((self.x)*(other.x) + (self.y)*(other.y))/(other.x**2 - other.y**2)
		y = ((other.x)*(self.y) - (self.x)*(other.y))/(other.x**2 - other.y**2)
		return Complex(x, y)

	def abs(self):
		return math.sqrt(self.x**2 + self.y**2)

def main():
	c1 = Complex(5.7, 99)
	c2 = Complex(3, 4.2)

	print("The complex numbers are: ")
	print(c1)
	print(c2)
	print("")

	print("Real Part of first complex number: ")
	print(c1.real())
	print("")

	print("Imaginary Part of second complex number: ")
	print(c2.imag())
	print("")

	print("Argument of the complex numers: ")
	print(c1.argument(), " and ", c2.argument())
	print("")

	print("Conjugate of the complex numers: ")
	print(c1.conjugate(), " and ", c2.conjugate())
	print("")

	print("Abslute values of the complex numbers")
	print(c1.abs(), " and ", c2.abs())
	print("")

	print("Addition of the two complex numbers: ")
	print(c1+c2)
	print("")

	print("Subtraction of the two complex numbers: ")
	print(c1-c2)
	print("")

	print("Multiplication of the two complex numbers: ")
	print(c1*c2)
	print("")

	print("Division of the two complex numbers:")
	print(c1/c2)
	print("")


main()
