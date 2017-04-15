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
		day = {}
		for j in range (0,(len(tmp)-3)/2):
			day[tmp[3+j*5]] = {}
			day[tmp[3+j*5]][j] = {}
		for j in range (0,(len(tmp)-3)/2):
			day[tmp[3+j*5][j][tmp[4+j*5]] = int(tmp[5+j*5])
			day[tmp[3+j*5][j][tmp[6+j*5]] = int(tmp[7+j*5])
		course = Course(tmp[0],int(tmp[1]),tmp[2],day)
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
