
import csv
import yaml

#####EMPLOYEES
employee_fields = ['address_id', 'department_id', 'employee_id', 'name', 'age', 'salary']

num_employees = int(input('How many employees are there? : '))

department_ids = {
  'Sales' : 1,
  'Development' : 2,
  'Accounting' : 3,
  'Human Resources' : 4,
  'Research' : 5,
  'CEO': 6

}
employee_rows = []
employee_ids = {}

for i in range(num_employees):
  employee_rows.append([])
  current = employee_rows[-1]
  print('Adding new employee')
  current.append(i + 1)
  current.append(department_ids[input("What is this employee's department? (Sales, Development, Accounting, Human Resources, Research, CEO): ")])
  current.append(i + 1)
  current.append(input("What is this employee's name? : "))
  current.append(input("What is this employee's age?: "))
  current.append(input("What is this employee's salary?: "))
  employee_ids[current[-3]] == current[0]

with open('employees_v2.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(employee_fields)

    # writing the data rows
    csvwriter.writerows(employee_rows)


#####DEPARTMENTS



department_fields = ['department_id', 'department_name', 'manager_id', 'address_id']

num_departments = int(input('How many departments are there? : '))


department_rows = []
address_counter = num_employees

for i in range(num_departments):
  department_rows.append([])
  current = department_rows[-1]
  print('Adding new department')
  current.append(i + 1)
  current.append(input("What is the name of this department? : "))
  current.append(employee_ids[input("Who is the manager for this department? : ")])
  current.append(address_counter)
  address_counter += 1



with open('departments_v2.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(department_fields)

    # writing the data rows
    csvwriter.writerows(department_rows)



###### ADDRESSES
address_fields = ['address_id', 'street', 'city', 'state']

num_addresses = num_employees + num_departments


address_rows = []

for i in range(num_addresses):
  address_rows.append([])
  current = address_rows[-1]
  print('Adding new address')
  current.append(i + 1)
  current.append(input("What is the street address for this address? : "))
  current.append(input("What is the city for this address? : "))
  current.append(input("What is the state for this address? : "))



with open('adresses_v2.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(address_fields)

    # writing the data rows
    csvwriter.writerows(address_rows)

