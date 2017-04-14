class Course:

	"""A Course such as those found on cunyfirst
	Attributes:
		title: A string that represents the name of the course e.g. CSC103 Intro to Computing for Majors
		nbr: An integer representing a unique id or number for the course.
		prof: A string representing the professor of the course.
		time: A dictionary of an array of tuples that is used to retrieve all of the course times. The first key is the day, the first index is the occurrence i.e. there are some courses that have different times on the same day, the second index is the start and end tuple. E.g. time["monday"][0][START] will return the start time for a Course's monday class.
	"""
	def __init__(self, title, nbr, prof, time):
		"""Inititalizes Course object"""
		self.title = title
		self.nbr = nbr
		self.prof = prof
		self.time = time
	def dayTimes(self, day):
		"""Returns a string array of all day times for the Course"""
		s = []
		for occurrences in time[day] :
		s.append("{}: {}-{}\n".format(day, occurrences[0], occurrences[1]))
		return s
	def courseNbr(self):
		"""Returns a string with nbr"""
		return "Course Number:{}".format(self.nbr)
		
