import csv


filename = "C:/Users/jiten/Desktop/python_work/codeacademyProjects/insurance.csv"

age = []
sex = []
bmi = []
num_of_children = []
smoker = []
region = []
charges = []

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	for row in reader:
		age.append(row[0])
		sex.append(row[1])
		bmi.append(row[2])
		num_of_children.append(row[3])
		smoker.append(row[4])
		region.append(row[5])
		charges.append(row[6])

# Now the data has been neatly organized into lists.
# One can beginn to initiaze the data.

class Patients:
	"""Initializing patients information."""
	def __init__(self, patientsAge, patientsSex, patientsBmi, patientsChildren, patientsIsSmoker
	, patientsRegion, patientsCharges):
		self.patientsAge = age
		self.patientsSex = sex
		self.patientsBmi = bmi
		self.patientsChildren = num_of_children
		self.patientsIsSmoker = smoker
		self.patientsRegion = region
		self.patientsCharges = charges

	def patientsinfo_dictonary(self):
		"""Organizing neat data into dictonary to analyze further if needed or asked.""" 
		self.patientsinfo = {}
		self.patientsinfo['Age'] = self.patientsAge
		self.patientsinfo['sex'] = self.patientsSex
		self.patientsinfo['bmi'] = self.patientsBmi
		self.patientsinfo['num_of_children'] = self.patientsChildren
		self.patientsinfo['smoker'] = self.patientsIsSmoker
		self.patientsinfo['region'] = self.patientsRegion
		self.patientsinfo['charges'] = self.patientsCharges
		return self.patientsinfo
	
	def analyze_age(self):
		"""Calculating average age in our dataset."""
		average_age = 0
		for age in self.patientsAge:
			average_age += int(age)

		print(f"The average age: {round(average_age/len(self.patientsAge), 2)}")
	


	def cost_average(self):
		"""Calculating average cost in the dataset."""
		total_cost = 0
		for cost in self.patientsCharges:
			total_cost += float(cost)
			# The average cost per person.
		print(f"The average cost: {round(total_cost/len(self.patientsCharges), 2)}")


	def analyze_gender(self):
		"""Caculating number of men and women in the dataset."""
		total_men = 0
		total_women = 0
		for i in self.patientsSex:
			if i == 'female':
				total_women += 1
			else:
				total_men += 1
		print(f"Total number of Women: {total_women}")
		print(f"Total number of Men: {total_men}")

	def analyze_smoker(self):
		"""Checking how many smoker or non smoker are in our dataset."""
		smokers = 0
		non_smokers = 0
		for smoker in self.patientsIsSmoker:
			if smoker == 'yes':
				smokers += 1
			else:
				non_smokers += 1

		print(f"The total number of Smokers: {smokers}")
		print(f"The total number of Non-Smokers: {non_smokers}")

# Calculating average children as compare to total number of patients.

	def average_children(self):
		"""Calculating average children per person."""
		total_children = 0
		for child in self.patientsChildren:
			total_children += int(child)

		print (f"Average Children: {(round(total_children / len(self.patientsChildren), 2))}")


	def analyze_region(self):
		"""Checking how many diffirent region are available in our data set."""
		region = []
		for area in self.patientsRegion:
			# Append only if area is not in our region already.
			if area not in region:
				region.append(area)	
		print(region)

		



# Creating a new variable to execute the class and call the function.
patients = Patients(age, sex, bmi, num_of_children, smoker, region, charges)
patients.analyze_age()
patients.analyze_gender()
patients.analyze_smoker()
patients.average_children()
patients.patientsinfo_dictonary()
patients.cost_average()
patients.analyze_region()

# If needed, One can further analyze data as asked.







