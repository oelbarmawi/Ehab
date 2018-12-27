# We define a function like so

def sendEmail(email, name, message):
	if checkParameters(email, name, message):
		# String concatenation
		statement = "I will send " + name + " this message: " + message + " to his email: " + email
		print(statement)
	else:
		print("You have given the wrong parameters.")
	

# Returns a boolean True/False
def checkParameters(s1, s2, s3):
	return type(s1) == str and type(s2) == str and type(s3) == int


sendEmail('ehab@gmail.com', 123, "Hello, I'm Omar")


