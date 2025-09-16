# Dictionaries in Python

A dictionary is:

A collection of key-value pairs.

Keys must be unique and immutable (str, int, tuple).

Values can be any data type.

## Creating a Dictionary

```py
student = {
    "name": "Alice",
    "age": 21,
    "marks": 85
}
print(student["name"])   # Alice

```
## Accessing & Updating
```py

# Accessing
print(student["age"])           # 21
print(student.get("marks"))     # 85
print(student.get("gender", "Not Found"))  # default value

# Updating
student["age"] = 22
student["gender"] = "Female"
print(student)

# o/p
{'name': 'Alice', 'age': 22, 'marks': 85, 'gender': 'Female'}


```

## Common Dictionary Methods
```py
print(student.keys())     # dict_keys(['name', 'age', 'marks', 'gender'])
print(student.values())   # dict_values(['Alice', 22, 85, 'Female'])
print(student.items())    # dict_items([('name', 'Alice'), ('age', 22), ...])

student.pop("marks")      # remove key
student.update({"city": "Delhi"})   # add/update multiple

```
## Looping through Dictionary

```py
for key, value in student.items():
    print(key, ":", value)

# o/p

name : Alice
age : 22
gender : Female
city : Delhi

```

| Feature          | Set                           | Dictionary            |
| ---------------- | ----------------------------- | --------------------- |
| Structure        | Unique, unordered elements    | Key-value pairs       |
| Duplicate values | ❌ Not allowed                | ✅ Values can repeat  |
| Indexing         | ❌ Not possible               | ✅ Possible via keys  |
| Use cases        | Removing duplicates, set math | Fast lookup, mappings |
