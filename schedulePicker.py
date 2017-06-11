from Course import Course

courses = []
schedules = [[]]
START = 0
END = 1

def initCourses(datain):
	time  = {}
	for i in range(1, (len(datain)-3)/3 + 1):
		dayIdx = 3*i
		if datain[dayIdx] not in time:
			time[datain[dayIdx]] = []
		occurrence = [int(datain[dayIdx+1]), int(datain[dayIdx+2])]
		time[datain[dayIdx]].append(occurrence)
	courses.append(Course(datain[0], int(datain[1]), datain[2], time))
def determineSchedules(courses):
	schedules = []
	for course in courses:
		possible = []
		possible.append(course)
		for othercourse in courses:
			overlap = False
			for established in possible:
				if determineOverlap(othercourse, established):
					overlap = True
					break
			if not overlap:
				possible.append(othercourse)
		possible.sort(key=lambda x: x.title)
		if possible not in schedules:
			schedules.append(possible)
	return schedules
def determineOverlap(course1, course2):
	for day in course1.time:
		if day in course2.time:
			for occurrence in course1.time[day]:
				for otheroccurrence in course2.time[day]:
					if occurrence[START] <= otheroccurrence[END] and occurrence[END] >= otheroccurrence[START]:
						return True
						"""print("Conflict on "+day+ " for course " + course1.title + " from " + str(occurrence[START]) + " to " + str(occurrence[END]) + " and course " + course2.title + " from " + str(otheroccurrence[START]) + " to " + str(otheroccurrence[END])  + ".")"""
def printSchedules(schedules):
	
def main(filename):
	data = '''get data from file'''
	initCourses(data)
	determineSchedules(courses)
	printSchedules(schedules)

main('''filename from terminal''')
