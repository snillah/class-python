import csv


data = [["Charmi",20,"A"],["Ravi",21,"B"]]

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["name","age","grade"]) # header
    writer.writerow(["Saravanan","21","A"]) # values
    writer.writerow(["Dhatree","25","A+"]) # values
    writer.writerows(data)

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Anu", 19, "A"])

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# in ML

# import csv
# import os

# # Folder path
# folder = "csv_folder"

# # Make sure folder exists
# os.makedirs(folder, exist_ok=True)

# # File path inside the folder
# file_path = os.path.join(folder, "data.csv")

# # Writing data
# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 25, "London"],
#     ["Bob", 30, "New York"],
#     ["Charlie", 28, "Paris"]
# ]

# with open(file_path, mode="w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print(f"CSV file written at: {file_path}")

#-------------------------------------------------------
# MultipleFiles
# import csv
# import os

# folder = "csv_folder"

# for filename in os.listdir(folder):
#     if filename.endswith(".csv"):
#         file_path = os.path.join(folder, filename)
#         print(f"\nReading {filename}:")
#         with open(file_path, mode="r", encoding="utf-8") as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 print(row)

#------------------------------------------------------------


# import csv
# import os

# folder = "csv_folder"
# os.makedirs(folder, exist_ok=True)

# datasets = {
#     "students.csv": [["ID", "Name"], [1, "Alice"], [2, "Bob"]],
#     "employees.csv": [["ID", "Role"], [101, "Manager"], [102, "Engineer"]],
# }

# for filename, data in datasets.items():
#     file_path = os.path.join(folder, filename)
#     with open(file_path, "w", newline="", encoding="utf-8") as f:
#         writer = csv.writer(f)
#         writer.writerows(data)
#     print(f"Written: {file_path}")

