class ClassifiedString:

	def __init__(self, rawClassifiedString):

		self.__string = ""
		self.__classifiedAsString = ""
		
		parsedLine = rawClassifiedString.split(" - ")
		
		if (len(parsedLine) > 1):
			
			self.__classifiedAsString = parsedLine.pop().rstrip()
			self.__string = " ".join(parsedLine)
			
		else:
			
			exceptionText = "ClassifiedString: Incorrect rawClassifiedString format (%s), must be something like this \"Metallica - metal\"" % (rawClassifiedString.rstrip())
			
			raise Exception(exceptionText)
		
	def string(self):
		
		return self.__string
	
	def classifiedAsString(self):
		
		return self.__classifiedAsString