import csv
file=open("google_stock_data.csv")
reader=csv.reader(file)
header=next(header)
print(header)
print(next(reader))
for row in reader:
    print(row[0])