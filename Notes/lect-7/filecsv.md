# File Handling with CSV and JSON

CSV Files (Comma-Separated Values)

A CSV file looks like this (students.csv):

```py
# file in csv
name,age,grade
Saravanan,20,A
Ravi,21,B
Anu,19,A

```
## Reading CSV

```py
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# o/p
['name', 'age', 'grade']
['Saravanan', '20', 'A']
['Ravi', '21', 'B']
['Anu', '19', 'A']

```
## Writing CSV
```py
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "age", "grade"])  # header
    writer.writerow(["Saravanan", 20, "A"])
    writer.writerow(["Ravi", 21, "B"])

```
## Appending to CSV
```py
import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Anu", 19, "A"])

```