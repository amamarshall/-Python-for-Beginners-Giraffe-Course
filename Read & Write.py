# open("employees.txt", "r+")
# open("employees.txt", "w")
# open("employees.txt", "a")
employee_file = open("employees.txt", "r")

#for employee in employee_file.readlines():
#    print(employee)
print(employee_file.read())

employee_file.close()


# employee_file = open("employees.txt", "a")
#
# employee_file.write("\nKelly - Customer Service")
#
# employee_file.close()

employee_file = open("employees1.txt", "w")

employee_file.write("\nKelly - Customer Service")

employee_file.close()