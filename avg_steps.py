from audioop import avg
import csv

infile = open("steps.csv", "r")
outfile = open("avg_steps.csv", "w")

csv_file = csv.reader(infile, delimiter=",")


next(csv_file)

months = ["January", "February", "March", "April", "May", "June", "July", "August",
"September", "October", "November", "December"]

i = 0
counter = 0
month  = 1

outfile.write("Month, Average Steps\n")


for record in csv_file:
    print(i)
    if float(record[0]) != month:
        month -= 1
        avg_steps = (counter/i)
        avg_steps = format(avg_steps, ",.2f")

        print(months[month] + ", " + str(avg_steps))

        outfile.write(months[month] + ", " + str(avg_steps) + "\n")
        month += 2
        i = 0
        counter = 0
    if float(record[0]) == month:
        counter += float(record[1])
        i += 1


month -= 1
avg_steps = (counter / i)
avg_steps = format(avg_steps, ",.2f")
print(months[month] + ", " + str(avg))
outfile.write(months[month] + ", "  + str(avg_steps) + "\n")


outfile.close()

