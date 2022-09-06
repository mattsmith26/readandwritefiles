import csv

infile = open("customers.csv", "r")

csv_file = csv.reader(infile, delimiter=",")
outfile = open("customer_country.csv", "w")

next(csv_file)

outfile.write("Full Name, Country\n")

i = 0
#print("Full Name ,", "Last Name ", "                  Country")
#print("-------------------------------------------")


for record in csv_file:
    full_name = record[1] + " " + record[2]

    #first_name = record[1]
    #last_name = record[2]

    country = record[4]
    i += 1



    outfile.write(full_name + "," + country + "\n")

outfile.close()


    #print(format(record[1], "10"), format(record[2], "12"), "\t", record[4])

print("")
print("Total number of customers:", i)
