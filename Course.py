class Course:
	
	title = "Default course name"
	nbr = 0
	prof = "Default professor name"
	time = [][][]

	def __init__(self,title,prof,day,start,end):
		self.title = title;
		self.prof = prof;
		self.time.append(day);
		self.time[0].append(start);
		self.time[0][0].append(end);
	def print():
		
