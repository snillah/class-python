# Single quotes
str1 = 'Python'

# Double quotes
str2 = "Programming"

# Triple quotes (multi-line string)
str3 = """This is 
multi-line 
string"""

print(str1)
print(str2)
print(str3)

text = "PYTHON"

# indexing
print(text[0])   # P  (first character)
print(text[3])   # H  (4th character)
print(text[-1])  # N  (last character)
print(text[-3])  # H  (third from last)

# sllicing
print(text[0:4])    # PYTH   (from index 0 to 3)
print(text[:3])     # PYT    (from start to index 2)
print(text[2:])     # THON   (from index 2 to end)
print(text[-4:-1])  # THO    (negative slice)
print(text[::-1])   # NOHTYP (reverse string)

age = 18

if age >= 18:
        print(True)
else:
        print(False)

# After if age >= 18: → the : means: “If this condition is true, run the indented block below.”

# After else: → the : means: “If the above condition is false, run the indented block below.”

# In other languages (like C, Java), we use { } braces to mark a block.
# In Python, we use colon : + indentation instead.
