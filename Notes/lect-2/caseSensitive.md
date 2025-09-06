# These are naming conventions (ways of writing multi-word identifiers like variable names, class names, or functions) to make code more readable and consistent.

1. Snake Case (snake_case)

Words are lowercase and separated by underscores \_.

Common in Python variables and functions.

```py
student_name = "John"
total_marks = 450

```

2. Camel Case (camelCase)

First word is lowercase, subsequent words start with uppercase letters.

Common in JavaScript variables and functions.

```py
studentName = "John"
totalMarks = 450

```

3. Pascal Case (PascalCase)

Every word starts with a capital letter (including the first).

Common in class names in Python, Java, C#.

```py
StudentName = "John"
totalMarks = 450


```

4. Kebab Case (kebab-case)

Words are lowercase, separated by hyphens (-).

Not allowed in Python variables (since - is subtraction),
but used in URLs, HTML, CSS class names.

```py
student-name
total-marks

```

5. Upper Snake Case (a.k.a. CONSTANT_CASE)

All letters are UPPERCASE, words separated by \_.

Common for constants in Python.

```py
PI_VALUE = 3.1416
MAX_LIMIT = 100

```

| Convention      | Example        | Usage                           |
| --------------- | -------------- | ------------------------------- |
| **snake_case**  | `student_name` | Python variables, functions     |
| **camelCase**   | `studentName`  | JavaScript, Java methods        |
| **PascalCase**  | `StudentName`  | Class names in Python, Java, C# |
| **kebab-case**  | `student-name` | HTML/CSS, URLs                  |
| **UPPER_SNAKE** | `MAX_VALUE`    | Constants in Python             |
