# 1 What is a String?

A string is a sequence of characters enclosed in single quotes ('), double quotes ("), or triple quotes (''' or """).

Strings are immutable (cannot be changed after creation).

## Creating String

```py
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

```

## Indexing in Strings

Indexing means accessing individual characters of a string using their position number.

Index starts from 0 (first character).

You can also use negative indexing (last character = -1).

```py
text = "PYTHON"

print(text[0])   # P  (first character)
print(text[3])   # H  (4th character)
print(text[-1])  # N  (last character)
print(text[-3])  # H  (third from last)
```
## Slicing in Strings

Slicing is used to extract a portion (substring) of a string.

Syntax:
    ` string[start:end:step] `

start → index where slice begins (inclusive)

end → index where slice ends (exclusive)

step → jump (default is 1)

```py
text = "PYTHON"

print(text[0:4])    # PYTH   (from index 0 to 3)
print(text[:3])     # PYT    (from start to index 2)
print(text[2:])     # THON   (from index 2 to end)
print(text[-4:-1])  # THO    (negative slice)
print(text[::-1])   # NOHTYP (reverse string)

```

String = sequence of characters.

Indexing → access single character (s[0], s[-1]).

Slicing → extract substring (s[1:4], s[::-1]).