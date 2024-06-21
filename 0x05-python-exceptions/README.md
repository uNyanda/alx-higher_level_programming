# 0x05. Python - Exceptions.

**This directory contains files that can be tested for 0x05. Python - Exceptions. .**

## Tasks

> [!IMPORTANT]
> Make the Python files executables using the following command:

`chmod +x <filename>`

> [!NOTE]
> If there aren't any main.py files provided for a task, use test files to run the program.


- **0. Safe list printing.**

   - :file_folder: : `0-safe_print_list.py`: Function prints `x` elements of a list.

- **1. Safe printing of an integers list.**

   - :file_folder: : `1-safe_print_integer.py`: Function prints an integer with `{:d}.format().`

- **2. Print and count integers.**

   - :file_folder: : `2-safe_print_list_integers.py`: Function prints the first `x` elements of a list and only integers

- **3. Integers division with debug.**

   - :file_folder: : `3-safe_print_division.py`: Function divides 2 integers and prints the result.

- **4. Divide a list.**

   - :file_folder: : `4-list_division.py`: Function divides element by element 2 lists.

- **5. Raise exception.**

   - :file_folder: : `5-raise_exception.py`: Function raises a type exception.

- **6. Raise a message.**

   - :file_folder: : `6-raise_exception_msg.py`: Function raises a name exception with a message.

- **7. Safe integer print with error message.**

   - :file_folder: : `100-safe_print_integer_err.py`: Function prints an integer.

- **8. Safe function.**

   - :file_folder: : `101-safe_function.py`: Function executes a function safely.

- **9. ByteCode-> Python #4.**

   - :file_folder: : `102-magic_calculation.py`: Function mimics Python byte code.

- **10. Cpython #2: PyFloatObject.**

   - :file_folder: : `103-tests.py`: Create three C functions that print some basic info about Python lists,  Python bytes, and Python float objects.

   - compilation: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c`
