# These are built-in methods that make string handling easier.

## upper()

    Converts the whole string into UPPERCASE.

```py
text = "Python Programming"
print(text.upper())

```
## lower()

Converts the whole string into lowercase.

```py
text = "Python Programming"
print(text.lower())

```
## replace(old, new)

Replaces all occurrences of a substring with another.

```py
text = "I like Java"
print(text.replace("Java", "Python"))
```
## split(separator)
Splits the string into a list of words using a separator (default: space).

```py
text = "apple,banana,cherry"
print(text.split(","))   # split by comma

```
## join()
Joins elements of a list/tuple into one string.

```py
words = ["Python", "is", "fun"]
result = " ".join(words)
print(result)

#o/p
Python is fun

```

strip() → removes spaces from start and end

title() → Capitalizes first letter of each word

find() → finds the position of substring

```py
text = "  hello world  "

print(text.strip())       # "hello world"
print(text.title())       # "Hello World"
print(text.find("world")) # 6

```




| Function    | Purpose              | Example                              |
| ----------- | -------------------- | ------------------------------------ |
| `upper()`   | Convert to uppercase | `"hi".upper()` → `"HI"`              |
| `lower()`   | Convert to lowercase | `"HI".lower()` → `"hi"`              |
| `replace()` | Replace substring    | `"hi".replace("hi","bye")` → `"bye"` |
| `split()`   | Split into list      | `"a b c".split()` → `['a','b','c']`  |
