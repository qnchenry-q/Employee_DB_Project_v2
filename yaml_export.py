import yaml
import csv

departments_d = {}
with open('departments_v2.csv') as csvf:
  reader = csv.DictReader(csvf)

  for rows in reader:
    key = rows['department_id']
    departments_d[key] = rows


  with open('employees_yaml.yaml', 'w') as file:
    file.write(yaml.dump(departments_d))

addresses_d = {}
with open('adresses_v2.csv') as csvf:
  reader = csv.DictReader(csvf)

  for rows in reader:
    key = rows['address_id']
    addresses_d[key] = rows


  with open('addresses_yaml.yaml', 'w') as file:
    file.write(yaml.dump(addresses_d))