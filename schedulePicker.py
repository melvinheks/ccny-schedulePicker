from Course import Course

courses = []
schedules = [[]]
START = 0
END = 1

def initCourses(datain):
	
def determineSchedules(courses):
	
def determineOverlap(course1, course2):
	for day in course1.time:
		if day in course2.time:
			for occurrence in course1.time[day]:
				for otheroccurrence in course2.time[day]:
					if occurrence[START] <= otheroccurrence[END] and occurrence[END] >= otheroccurrence[START]:
						return True
						"""print("Conflict on "+day+ " for course " + course1.title + " from " + str(occurrence[START]) + " to " + str(occurrence[END]) + " and course " + course2.title + " from " + str(otheroccurrence[START]) + " to " + str(otheroccurrence[END])  + ".")"""
def printSchedules(schedules):
	
def main(datain):
	data = '''get data from file'''
	initCourses(data)
	determineSchedules(courses)
	printSchedules(schedules)

main('''input from textfile''')
