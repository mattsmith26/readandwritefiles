import csv
from types import CoroutineType

infile = open("customers.csv", "r")


csv_file = csv.reader(infile, delimiter=",") # how pyhton knows to seperate csv file with comma

next(csv_file) # this will skip the first row

for record in csv_file:

    id = record[0]
    first_name = record[1]
    last_name = record[2]
    city = record[3]
    country = record[4]
    phone = record[5]

    
    print("ID:", id)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("City:", city)
    print("Country:", country)
    print("Phone:", phone)

    input()




