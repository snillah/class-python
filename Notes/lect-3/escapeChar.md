# Common Escape Characters in Python

| Escape | Meaning                                 | Example             | Output           |
| ------ | --------------------------------------- | ------------------- | ---------------- |
| `\'`   | Single quote                            | `'It\'s fine'`      | `It's fine`      |
| `\"`   | Double quote                            | `"He said \"Hi\""`  | `He said "Hi"`   |
| `\\`   | Backslash                               | `"C:\\Users\\Name"` | `C:\Users\Name`  |
| `\n`   | New line                                | `"Hello\nWorld"`    | Hello <br> World |
| `\t`   | Tab space                               | `"Hello\tWorld"`    | Hello    World   |
| `\b`   | Backspace                               | `"Hello\bWorld"`    | HellWorld        |
| `\r`   | Carriage return (moves cursor to start) | `"Hello\rWorld"`    | World            |
| `\f`   | Form feed (page break, rarely used)     | –                   | –                |
| `\ooo` | Octal value                             | `"\110\145"`        | He               |
| `\xhh` | Hex value                               | `"\x48\x65"`        | He               |

# Raw Strings (ignore escape characters)

If you don’t want escape characters to work, prefix string with r.

```py
path = r"C:\Users\Name\Documents"
print(path)

# o/p
C:\Users\Name\Documents

```

Escape sequences allow special characters inside strings.

Most common: \n, \t, \", \\.

Use r"string" for raw strings (ignores escapes).