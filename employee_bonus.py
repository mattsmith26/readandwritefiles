import csv

infile = open("EmployeePay.csv", "r")

csv_file = csv.reader(infile, delimiter=",")

next(csv_file)


for record in csv_file:

    id = record[0]
    full_name = record[1] + " " + record[2]
    salary = float(record[3])
    bonus = (float(record[4]) * 100)

    total_pay = format( salary + (salary * bonus), "," ) 

    print("ID:", id)
    print("Full Name:", full_name)
    print("Salary:", format(salary, ","))
    print("Bonus: " + str(int(bonus)) + "%")
    print("Total Pay: " + "$" + str(total_pay))
    

    input()

