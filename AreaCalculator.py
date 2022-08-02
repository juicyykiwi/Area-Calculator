from math import pi, sqrt

# Name: Ray-Ann Pappas
# Date: 8/1/22

class Calculator:
	shape = "0"		# Every calculator object must have a shape variable, declared outside of all methods

	# Main method
	def main(self):
			print("Welcome to AREA CALCULATOR!")
			self.getArea()

	# Method calculating area of circle
	def circle(self, circle):
			self.area = (circle * circle) * pi 		# Radius squared * PI = Area
			return self.area

	# Method calculating area of circle
	def square(self, square):
			self.area = (square * square)			# Length * width = Area, L = W with squares
			return self.area
	
	def rectangle(self, length, width):				
			self.area = (length * width)			# Length * width = Area
			return self.area

	def triangle(self, base, height):				
			self.area = (0.5 * (base * height))		# 1/2 * (Base * height) = Area
			return self.area

	def parallelogram(self, base, height):	
			self.area = base * height				# b * h = A
			return self.area

	def cylinder(self, radius, height):
			self.area = (2 * (pi * (radius * height))) + (2 * (pi * (radius * radius))) 	# 2*PI*r*h + 2*PI*r² = A
			return self.area

	def semicircle(self, semicircle):
			self.area = ((semicircle * semicircle) * pi) * 0.5		# r² * PI * 1/2 = A
			return self.area

	def kite(self, diag1, diag2):
			self.area = (diag1 * diag2)/2			# (p * q) / 2 = A
			return self.area

	def pentagon(self, pentagon):
			self.area = 0.25 * sqrt(5 * (5 + (2 * sqrt(5)))) * (pentagon * pentagon)		# 1/4 * √(5(5+2√(5))) * a² = A
			return self.area

	def hexagon(self, hexagon):
			self.area = ((3 * sqrt(3))/2) * (hexagon * hexagon)		# ((3 * √3) / 2) * a² = A
			return self.area

	def octagon(self, octagon):
		self.area = 2 * (1 + sqrt(2)) * (octagon * octagon)			# 2 * (1 + √2) * a² = A
		return self.area

	def trapezoid(self, base1, base2, height):
		self.area = ((base1 + base2)/2) * height	# ((a + b) / 2) * h = A
		return self.area

	# Method that prompts user with area calculation menu, calculates area
	def getArea(self):
		print("\nWhat is the preferred unit of measurement for this calculation? (Type abbreviated)")
		self.unit = input()
		print("\nThe unit you entered was: "+self.unit)
		print("Is this correct? (Y/N)")
		answer = input()
		while (answer != "Y" and answer != "y"):
			if (answer == "N" or answer == "n"):
				print("\nWhat is the preferred unit of measurement for this calculation? (Type abbreviated)")
				self.unit = input()
				print("\nThe unit you entered was: "+self.unit)
				print("Is this correct? (Y/N)")
				answer = input()
			elif (answer != "Y" and answer != "y" and answer != "N" and answer != "n"):
				print("\nPlease enter a valid response.")
				print("The unit you entered was: "+self.unit)
				print("Is this correct? (Y/N)")
				answer = input()

		print("\nPlease select the type of shape you would like to find the area of:")
		print("1.) Circle\t2.) Square\t3.) Rectangle\t4.) Trapezoid\t5.) Triangle\t6.) Semi-circle")
		print("7.) Cylinder\t8.) Kite\t9.) Pentagon\t10.) Hexagon\t11.) Octagon\t12.) Parallelogram")
		# User enters number assosciated with shape, stored in shape variable
		self.ashape = input()

		if (self.ashape == "1"):
			# If the choice is circle...
			print("\nPlease enter the radius of your circle.")
			self.r = int(input())     # Radius
			self.circle(self.r)
			self.a = str(round(self.circle(self.r), 2))   # Area, Calls Circle method, rounds to 2 decimal places
			print("\nThe area of your circle is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "2"):
			# If the choice is square...
			print("\nPlease enter one side length of your square.")
			self.l = int(input())
			self.a = str(round(self.square(self.l), 2))   # Area, Calls Square method, rounds to 2 decimal places
			print("\nThe area of your square is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "3"):
			print("\nPlease enter the length of your rectangle.")
			self.l = int(input())
			print("\nPlease enter the width of your rectangle.")
			self.w = int(input())
			self.a = str(round(self.rectangle(self.l, self.w), 2))   # Area, Calls Rectangle method, rounds to 2 decimal places
			print("\nThe area of your rectangle is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "4"):
			print("\nPlease enter the first base of your trapezoid.")
			self.b1 = int(input())
			print("\nPlease enter the second base of your trapezoid.")
			self.b2 = int(input())
			print("\nPlease enter the height of your trapezoid.")
			self.h = int(input())
			self.a = str(round(self.trapezoid(self.b1, self.b2, self.h), 2)) 	# Area, Calls Trapezoid method, rounds to 2 decimal places
			print("\nThe area of your trapezoid is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "5"):
			print("\nPlease enter the base length of your triangle.")
			self.b = int(input())
			print("\nPlease enter the height of your triangle.")
			self.h = int(input())
			self.a = str(round(self.triangle(self.b, self.h), 2))   # Area, Calls Triangle method, rounds to 2 decimal places
			print("\nThe area of your triangle is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "6"):
			print("\nPlease enter the radius of your semi-circle.")
			self.r = int(input())
			self.a = str(round(self.semicircle(self.r), 2))   # Area, Calls Semicircle method, rounds to 2 decimal places
			print("\nThe area of your semi-circle is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "7"):
			print("\nPlease enter the radius of your cylinder.")
			self.r = int(input())
			print("\nPlease enter the height of your cylinder.")
			self.h = int(input())
			self.a = str(round(self.cylinder(self.r, self.h), 2))   # Area, Calls Cylinder method, rounds to 2 decimal places
			print("\nThe area of your cylinder is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "8"):
			print("\nPlease enter the length of the first diagonal of your kite.")
			self.d1 = int(input())
			print("\nPlease enter the length of the second diagonal of your kite.")
			self.d2 = int(input())
			self.a = str(round(self.kite(self.d1, self.d2), 2)) 	# Area, Calls Kite method, rounds to 2 decimal places
			print("\nThe area of your kite is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "9"):
			print("\nPlease enter the apothem of your pentagon.")
			self.ap = int(input())
			self.a = str(round(self.pentagon(self.ap), 2)) 	# Area, Calls Pentagon method, rounds to 2 decimal places
			print("\nThe area of your pentagon is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "10"):
			print("\nPlease enter the apothem of your hexagon.")
			self.ap = int(input())
			self.a = str(round(self.hexagon(self.ap), 2)) 	# Area, Calls Hexagon method, rounds to 2 decimal places
			print("\nThe area of your hexagon is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "11"):
			print("\nPlease enter the apothem of your octagon.")
			self.ap = int(input())
			self.a = str(round(self.octagon(self.ap), 2)) 	# Area, Calls Octagon method, rounds to 2 decimal places
			print("\nThe area of your hexagon is: "+self.a+" "+self.unit+"²")
		elif (self.ashape == "12"):
			print("\nPlease enter the base length of your parallelogram.")
			self.b = int(input())
			print("\nPlease enter the height of your parallelogram.")
			self.h = int(input())
			self.a = str(round(self.parallelogram(self.b, self.h), 2))   # Area, Calls Parallelogram method, rounds to 2 decimal places
			print("\nThe area of your parallelogram is: "+self.a+" "+self.unit+"²")
		else:
			print("\nThere is no shape assosciated with your choice. Please try again.")

		print("\nWould you like to calculate the area of another shape? (Y/N)")
		answer = input()
		if answer == "N" or answer == "n":
			print("\nThank you for using AREA CALCULATOR!")
		elif answer == "Y" or answer == "y":
			self.getArea()
		else:
			while answer != "Y" and answer != "y" and answer != "N" and answer != "n":
				print("\nPlease enter a valid response. ")
				print("Would you like to calculate the area of another shape? (Y/N)")
				answer = input()
				if answer == "N" or answer == "n":
					print("\nThank you for using AREA CALCULATOR!")
				elif answer == "Y" or answer == "y":
					self.getArea()

if __name__ == "__main__":
	calc = Calculator()
	calc.main()
# This always runs the main method when the code is executed
