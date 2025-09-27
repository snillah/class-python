JSON Files (JavaScript Object Notation)

A JSON file (student.json) looks like this:

{
  "name": "Saravanan",
  "age": 20,
  "grade": "A"
}

Reading JSON
import json

with open("student.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data["name"])


✅ Output:

{'name': 'Saravanan', 'age': 20, 'grade': 'A'}
Saravanan

Writing JSON
import json

student = {
    "name": "Ravi",
    "age": 21,
    "grade": "B"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


✅ File saved as pretty JSON:

{
    "name": "Ravi",
    "age": 21,
    "grade": "B"
}

Appending JSON (read → modify → write back)
import json

with open("students.json", "r") as file:
    data = json.load(file)

data.append({"name": "Anu", "age": 19, "grade": "A"})

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)


⚡ Summary

CSV → like Excel sheets, use csv module.

JSON → structured data, use json module.

Both are extremely common in real-world Python projects (APIs, data storage, configs).