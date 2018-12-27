class Dog():

	#Constructor - necessary attributes that need to be passed in
	def __init__(self, weight, age, color):
		#Instance Variables
		self.a = age
		self.w = weight
		self.c = color

	#Instance Methods
	def getWeight(self):
		return self.w

	def getAge(self):
		return self.a

	def getColor(self):
		return self.c

	def speak(self, phrase):
		print(phrase)



bob = Dog(100, 2, "red")
print("Bob's age is:", bob.getAge())
print("Bob's color is:", bob.getColor())
bob.speak("Hello my name is Bob")




