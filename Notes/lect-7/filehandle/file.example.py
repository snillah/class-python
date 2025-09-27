import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])  # header
    writer.writerow(["Saravanan", 20, "A"])
    writer.writerow(["Ravi", 21, "B"])

    
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)