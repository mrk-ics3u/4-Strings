# Lab 4 - Password Checker

The line that asks for the password (`Enter password: `) is already in
`main.py`. Leave it as it is.

Open `main.py` and complete the following:

1. Update the header with your information (Name, Purpose, Author, Created, Updated).
2. If `password` is shorter than 8 characters, print `Error: Password must be at least 8 characters long.`
3. If `password` has no lowercase letter, print `Error: Password must contain at least one lowercase letter.`
4. If `password` has no uppercase letter, print `Error: Password must contain at least one uppercase letter.`
5. If `password` does not contain exactly one digit, print `Error: Password must contain exactly one digit.`
6. If none of the errors above apply, print `Password is valid.`

Print every error that applies, in the order above, one per line. For example,
the password `hi` prints:

```
Error: Password must be at least 8 characters long.
Error: Password must contain at least one uppercase letter.
Error: Password must contain exactly one digit.
```

## Running your program

Open `main.py` and press the Run button in the top right corner of VS Code. Your output appears in the terminal at the bottom.

## Checking your work

Press **Ctrl+Shift+B** to run the tests. You will see one line per test:

```
[PASS] 1. Header is filled in
[FAIL] 2. Valid password
```

When a test fails it shows what was expected and what your program printed. Fix your code and press Ctrl+Shift+B again. Keep going until all tests pass.

## Reminders

- Fill in every field of the header before you write any code.
- Write comments as you go. One comment per check is a good start.
- Tests check your output exactly. Copy each message exactly, including `Error: ` and the period.
- Use separate `if` statements (not `elif`) so that more than one error can print.
