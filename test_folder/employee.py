class Employee():
	"""docstring for Employee"""
	def __init__(self, first_name, last_name, annual_salary = ''):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def employee_details(self):
		full_name = self.first_name + " " + self.last_name
		return full_name



	def give_raise(self,raises = ''):
		if raises:
			self.annual_salary += raises
		else:
			self.annual_salary += 5000

		return self.annual_salary


Employee('Ben','Dankyi' ,60000)
my_employee = Employee.employee_details('self')
		
		