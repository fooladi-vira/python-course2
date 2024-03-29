import csv
#read
with open('cancer.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

#write
with open('file.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Age', 'City'])
    csv_writer.writerow(['John', '30', 'New York'])
    csv_writer.writerow(['Mary', '25', 'London'])

