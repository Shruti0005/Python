service_year = int(input("How many year you have done your service in this company? "))
emp_salary = int(input("Enter your salary: "))
bonus = 0
if service_year > 5:
    bonus = emp_salary * 0.1
    emp_salary += bonus
    print(f"Including bonus your salary is {emp_salary}")
else:
    print("Sorry! you are not eligible for bonus.")
