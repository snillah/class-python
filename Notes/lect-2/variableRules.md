# Rules for Naming Variables

## Allowed characters → Letters (A–Z, a–z), Digits (0–9), Underscore (_)

Example: age, student_name, mark1

❌ Cannot start with a number

❌ 1student = "Raj" → Invalid

✅ student1 = "Raj"

## Case-sensitive

age and Age are different variables.

❌ No spaces allowed

❌ student name = "Raj"

✅ student_name = "Raj"

## Cannot use reserved keywords (like for, if, while, class, etc.)

❌ for = 10 → Invalid

✅ Should be meaningful

Better to use student_age instead of x1y2z3.

```py
# valid names
name = "John"
student_age = 20
total_marks = 450
pi_value = 3.14

# invalid names
2value = 100      # starts with number ❌
my-name = "Raj"   # contains hyphen ❌
class = "Math"    # keyword ❌
```