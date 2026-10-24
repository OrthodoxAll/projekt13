import csv

# with open('students.csv') as st_file:
#     reader = csv.DictReader(st_file)
#     # next(reader)
#     for row in reader:
#         if float(row['avg_grade']) > 4.5:
#             print(row)


#
# with open('students.csv') as st_file:
#     reader = csv.reader(st_file)
#     # next(reader)
#     for row in reader:
#         # if float(row[2]) > 4.5:
#             print(row)




rows =[['name','age','avg_grade'],
        ['Grace', '26', '4.2'],
        ['Hannah', '27', '4.5'],
        ['Ian', '28', '4.1'],
        ['Jane', '29', '4.0'],
        ['Karl', '30', '4.6'],
        ['Laura', '31', '1.3'],
        ['Mike', '32', '1.7'],
        ['Nina', '33', '1.4'],
        ['Oscar', '34', '4.8']]

with open('students.csv', 'w', newline='') as st_file:
    writer = csv.writer(st_file)
    writer.writerow(rows)