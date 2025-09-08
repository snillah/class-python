🔹 What is Indentation?

Indentation means spaces at the beginning of a line.
Unlike other languages (like C, Java, etc.) that use { } or ; for blocks, Python uses indentation to indicate a block of code.

🔹 Example without indentation (Error ❌)
if True:
print("Hello")   # ❌ IndentationError

🔹 Correct Indentation
if True:
    print("Hello")   # ✅ Indented properly
    print("World")   # ✅ Part of same block


Output:

Hello
World

🔹 Indentation Rules

Default indentation is 4 spaces (PEP 8 standard).

You can also use a Tab, but mixing tabs and spaces is not recommended.

All statements inside a block must have the same indentation.

✅ Example:

for i in range(3):
    print("Number:", i)   # correct


❌ Wrong (uneven indentation):

for i in range(3):
  print("Hello")    # 2 spaces
    print("World")  # 4 spaces (error)

🔹 Nested Indentation

You can add multiple levels:

for i in range(3):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

🔹 Why Indentation is Important?

It makes code clean and readable.

Defines scope of loops, functions, conditions, classes, etc.

Summary:

Python uses indentation instead of curly braces {}.

Standard → 4 spaces per level.

Indentation errors are common for beginners.