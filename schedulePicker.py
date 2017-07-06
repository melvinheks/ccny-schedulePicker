from Course import Course
import fileinput

START = 0
END = 1

def initCourses(datain):
	"""Returns all Courses by initializing from datain 
		
		Args:
			datain (str[][]):
				[i][0] == title
				[i][1] == nbr
				[i][2] == prof
				[i][3],[i][4],[i][5], etc. == day,start,end, day,start,end, ... 

		Returns:
			courses (Course[]): 2d list of courses
	"""
	courses = []
	for course in datain:
		time  = {}
		for i in range(1, int((len(course)-3)/3) + 1):
			dayIdx = 3*i
			if course[dayIdx] not in time:
				time[course[dayIdx]] = []
			occurrence = [int(course[dayIdx+1]), int(course[dayIdx+2])]
			time[course[dayIdx]].append(occurrence)
		courses.append(Course(course[0], int(course[1]), course[2], time))
	return courses
# I want to rewrite this function in such a way that it does not need to check for duplicates
def determineSchedules(courses):
	"""Returns all relevant schedules based on courses
		
		Args:
			courses (Course[]): The courses of which schedules should be made from

		Returns:
			schedules (Course[][]): List of schedules
	"""
	schedules = []
	for course in courses:
		possible = []
		possible.append(course)
		for othercourse in courses:
			overlap = False
			for established in possible:
				if othercourse.title == established.title or determineOverlap(othercourse, established):
					overlap = True
					break
			if not overlap:
				possible.append(othercourse)
		possible.sort(key=lambda x: x.title)
		if possible not in schedules:
			schedules.append(possible)
	return schedules
def determineOverlap(course1, course2):
	"""Returns whether or not the two courses have any time conflicts or "overlaps"
		
		Returns:
			bool: True if there is an overlap, False otherwise
	"""
	for day in course1.time:
		if day in course2.time:
			for occurrence in course1.time[day]:
				for otheroccurrence in course2.time[day]:
					if occurrence[START] <= otheroccurrence[END] and occurrence[END] >= otheroccurrence[START]:
						return True
						#print("Conflict on "+day+ " for course " + course1.title + " from " + str(occurrence[START]) + " to " + str(occurrence[END]) + " and course " + course2.title + " from " + str(otheroccurrence[START]) + " to " + str(otheroccurrence[END])  + ".")
#This prints ugly text, rewrite
def printSchedules(schedules):
	"""Prints the schedules in an easy to read and appealing format
		
		Args: 
			schedules (Course[][]): List of schedules
	"""
	for schedule in schedules:
		print("Schedule\n")
		for course in schedule:
			print(course.title, course.time)
		print("\nEnd\n\n")
def getDataFromFile():
	"""Reads from the file specified from command line arg and returns a 2d list of strings in the correct order

		Returns:
			data: 2d list of strings which are of the the initCourse format
	"""
	days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
	data = []
	courseinput = []
	with fileinput.input() as filedata:
		for line in filedata:
			if not line[0].isspace():
				if	"Collapse" in line:
					title = line[17:line.index("-")-1]
				elif "Class" in line:
					nbr = next(filedata)
				elif "Open" in line or "Closed" in line:
					courseinput.insert(0, prof)
					courseinput.insert(0, nbr)
					courseinput.insert(0, title)
					data.append(courseinput)
					courseinput = []
				else:
					for day in days:
						if day in line:
							while not line[0].isspace():
								courseinput.extend(parseTimeStr(line))
								line = next(filedata)
							line = next(filedata)
							while not line[0].isspace():
								line = next(filedata)
							line = next(filedata)
							prof = line
							break
	return data
def parseTimeStr(timeStr):
	"""Reads a line from cuny first and returns a list with the correct formatting for a Course

	Args:
		timeStr: line from cunyfirst that has course times

	Returns:
		inputArr: list of strings	
	"""
	days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
	timein = timeStr.split()
	inputArr = []
	startTime = convertTimeToInt(timein[1])
	endTime = convertTimeToInt(timein[3])
	for day in days:
		if day in timein[0]:
			inputArr.append(day)
			inputArr.append(startTime)
			inputArr.append(endTime)
	return inputArr
def convertTimeToInt(twelveStr):
	"""Reads a twelve hour time and converts it to a 24 hour integer

		Args:
			twelveStr: string of the format x:xxAM|PM

		Returns:
			converted: 24 hour integer conversion of 12 hour format
	"""
	colonLoc = len(twelveStr)-5
	converted = int(twelveStr[0:colonLoc] + twelveStr[colonLoc+1:len(twelveStr)-2])
	if "PM" in twelveStr and (converted<1200 or converted>1299):
		converted += 1200
	return converted
def main():
	"""Calls corresponding functions from parsing input to printing out the schedules"""
	data = getDataFromFile()
	courses = initCourses(data)
	schedules = determineSchedules(courses)
	schedules.sort(key=lambda x: len(x), reverse=True)
	printSchedules(schedules)
if __name__ == "__main__":
	main()
