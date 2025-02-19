# Python-Projects-Beginner-Friendly
Small Python projects for Beginner to help utilize new python skills. 


Nice to knows:  

	if __name__ == '__main__': 

How It Works:

"__name__" is a special built-in variable in Python. When a Python file is executed directly, "__name__" is set to "__main__". When the file is imported into another script, __name__ is set to the filename (without .py).This checks whether the script is running as the main program. If true, the indented code block runs.

Why is This Useful?
1. If this script is imported into another program, the password won’t auto-generate.
2. If the script is run directly, it will generate and display a password.
3. This is a best practice in Python programming for writing reusable code.