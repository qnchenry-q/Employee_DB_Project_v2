import yaml
import csv
import pandas as pd

departments_d = {}
with open('departments_v2.csv') as csvf:
  reader = csv.DictReader(csvf)

  for rows in reader:
    key = rows['department_id']
    departments_d[key] = rows


  with open('employees_yaml.yaml', 'w') as file:
    file.write(yaml.dump(departments_d))

t_df = pd.read_csv('adresses_v2.csv')

grouped = t_df.groupby(['state', 'city'])

final = t_df.set_index(['state', 'city', 'address_id']).sort_values(['state', 'city','address_id'])

final.to_csv('grouped_adresses.csv')

ad = {}
with open('grouped_addresses.csv') as csvf:
    reader = csv.DictReader(csvf)
    for row in reader:
        state = row.pop("state")
        city = row.pop("city")
        if state not in ad:
            ad[state] = {city: [{row['address_id']: row['street']}]}
        else:
            if city in ad[state]:
                ad[state][city].append({row['address_id']: row['street']})
            else:
                ad[state].update({city: [{row['address_id']: row['street']}]})
with open('grouped_addresses.yaml', 'w') as file:
    file.write(yaml.dump(ad))
