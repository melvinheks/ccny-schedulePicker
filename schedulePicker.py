from .Course import Course

courses = []
schedules = [][]

def initCourses(datain):
	file1 = open(datain,"r");
	classes = []
	while true:
		data = file1.readline()
		if(data == ""):
			break;
		classes.append(data);
	for i in range (0,len(classes)):
		tmp = classes[i].split()
		course = Course(tmp[0],tmp[1],tmp[2],tmp[3]);
		courses.append(course);	
	file1.close()				
def determineSchedules(courses):
	
def determineOverlap(course1, course2):
	
def printSchedules(schedules):
	
def main(datain):
	data = '''get data from file'''
	initCourses(data)
	determineSchedules(courses)
	printSchedules(schedules)

main('''input from textfile''')
