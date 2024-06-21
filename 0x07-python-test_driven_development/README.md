# 0x07. Python - Test Driven Development

**This directory contains files that can be tested for 0x07. Python - Test Driven Development .**

> [!IMPORTANT]
> Make the Python files executables using the following command:
> `chmod +x <filename>`


## Tasks

> [!NOTE]
> If there aren't any main.py files provided for a task, use test files to run the program.
> Test files are stored in the folder **tests**


- [x] 0. **Integers addition**

  - :file_folder: : `0-add_integer.py` `tests/0-add_integer.txt` : Write a function that adds 2 integers

    - Prototype: _`def add_integer(a, b=98):`_
    - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message **`a must be an integer or b must be an integer`**
    - `a` and `b` must be first casted to integers if they are float
    - Returns an integer: the addition of `a` and `b`
    - You are not allowed to import any module
