import csv

employees = open('employee_file.csv')
print(employees.read())

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

fields = []
rows = []

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    fields = next(csv_reader)

    print(fields)

    for row in csv_reader:
        rows.append(row)

    for row in rows:
        print(row)
    

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Name', 'Department', 'Month Started'])
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

fields = ['Name', 'Department', 'Month Started']
rows = [['John Smith', 'Accounting', 'November'], ['Erica Meyers', 'IT', 'March']]

with open('employee_file.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

