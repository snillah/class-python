
print("""
      ADD,
      Edit,
      Delete,
      View => CRUD operations
      """)

para = []

while 1:
    # c = int(input("Select your choice : "))
    line = input()
    if line == "":
        break
    para.append(line)



print(" ".join(para))