MAX_ALLOWED_HOURS = 80


def manager(MAX_ALLOWED_HOURS):
	RATE = 35
	hours_worked = int(input("please how many hours did you work?: "))
	if hours_worked > MAX_ALLOWED_HOURS:
		over_time_pay = (hours_worked - MAX_ALLOWED_HOURS) * (RATE * 3)
		normal_time_pay = (MAX_ALLOWED_HOURS * RATE)
		total_pay = (over_time_pay + normal_time_pay)
	else:
		total_pay = (hours_worked * RATE)

	return total_pay


def employee(MAX_ALLOWED_HOURS):
	RATE = 15
	hours_worked = int(input("please how many hours did you work?: "))
	if hours_worked > MAX_ALLOWED_HOURS:
		over_time_pay = (hours_worked - MAX_ALLOWED_HOURS) * (RATE * 3)
		normal_time_pay = (MAX_ALLOWED_HOURS * RATE)
		total_pay = (over_time_pay + normal_time_pay)
	else:
		total_pay = (hours_worked * RATE)

	return total_pay


def tax(total_pay):
	if total_pay < 1000:
		print("No tax ")
		net_salary = total_pay
	elif total_pay >= 1000 or total_pay < 5000:
		net_salary = (total_pay - (total_pay*0.2))
	elif total_pay >= 5000 or total_pay < 10000:
		net_salary = (total_pay - (total_pay*0.25))
	else:
		net_salary = (total_pay - (total_pay*0.3))

	return net_salary

def main(worker):
	if worker == 'M' or worker == "MANAGER":
		total_pay = manager(MAX_ALLOWED_HOURS)
		print(f"Your total salary is {total_pay}")
		net_salary = tax(total_pay)
		print(f"After tax you were left with {net_salary}")
	else:
		total_pay = employee(MAX_ALLOWED_HOURS)
		print(f"Your total salary is {total_pay}")
		net_salary = tax(total_pay)
		print(f"After tax you were left with {net_salary}")

worker = input("Please what type of worker are you Manager or Emplyoyee: ").upper()

main(worker)













