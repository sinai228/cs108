'''This program is to calculate employees.
Created Fall 2018
Lab 09
Sebene Yi (ssy3) and Sinai Park (sp46)
'''

# importing
from employee import Employee

# Initiating 
employees = []

# Opening the text file to configure
with open('employees.txt', 'r') as file:
    for line in file:
        new = Employee(line)
        employees.append(new)

# exercise 9.4 printing the length of the list to make sure it is the same length as the employees.txt file        
#print(len(employees))

# Computing with the employees list
if len(employees) == 0:
    print("No employees, *****!")
if len(employees) >= 1:
    totals = {}
    counts = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for x in employees:
        if x.get_rank() in totals and x.get_rank() in counts:
            totals[x.get_rank()] += x.get_salary()
            counts[x.get_rank()] += 1
        else:
            totals[x.get_rank()] = x.get_salary()
            counts[x.get_rank()] = 1
        # Comparing and getting the maximum and minimum paid employees
        if x.get_salary() >= max_employee.get_salary():
            max_employee = x 
        elif x.get_salary() <= min_employee.get_salary():
            min_employee = x

    # Writing all the information into another text file
    file = open('employees_stats.txt', 'w')
 
    def print_average(totals, counts, file):
        '''This function will print average salaries according to rank'''
        file.write('Rank\tAverage\tSalary\n')
        for x in totals:
            average = totals[x] / counts[x]
            file.write(x + '\t' + str(average) + '\n')
        file.write("The highest paid person is: " + str(max_employee) + '\nThe lowest paid person is : ' + str(min_employee))
 
        file.close()

print_average(totals, counts, file)

