import csv
csv_columns = ['No','Name','Place']
dict_data = [
{'No': 1 ,'Name': 'KARTHIK' ,'Place': 'KERALA'},
{'No': 2  ,'Name': 'ARYAN' ,'Place': 'KARNATAKA'},
{'No': 3  ,'Name': 'SHAHID', 'Place': 'JAMMU & KASHMIR'},
{'No': 4 ,'Name': 'MANAV' ,'Place': 'MAHARASHTRA'},
{'No': 5 ,'Name': 'MEGHAL' ,'Place': 'DELHI'},
]
csv_file = "names.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)


with open('names.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row) 