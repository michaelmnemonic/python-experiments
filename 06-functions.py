# This file is for learning about functions in Python. Functions are reusable blocks of code that perform specific tasks. They help organize code, make it more readable, and allow for code reuse.

def print_hello_world():
    print("Hello World!")

def print_hello_world_multiple_time(times):
    for i in range(times):
        print("Hello World!")

def maximum(a, b):
    if a < b:
        return b
    else:
        return a

def main():
    print("Start of the script.")
    print_hello_world()
    print_hello_world_multiple_time(5)
    print(str(maximum(5, 19)))


# The code snippet:
#
# if __name__ == "__main__":
#     main()
#
# is a common Python idiom used to control the execution of code based on how the script is used:
#
# When the script is run directly (e.g., python 06-functions.py), the __name__ variable is set to "__main__", so the  main() function will execute.
#
# When the script is imported as a module (e.g., import 06_functions), the __name__ variable will be set to the module's name ("06_functions"), so the main() function will not execute.
#
# Purpose
# This pattern allows:
# - the script to be reusable as a module (without running main()  automatically).
# - a clear entry point for standalone execution.
# - separation of "test/execution code" from "library code".
if __name__ == "__main__":
    main()