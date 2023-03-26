# 0x02. Python - import & modules
### Tasks
**0. Import a simple function from a simple file**

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
- You have to use `print` function with string format to display integers
- You have to assign:
	- the value `1` to a variable called `a`
	- the value `2` to a variable called b
	- and use those two variables as arguments when calling the functions `add` and `print`
`a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
- You can only use the word `add_0` once in your code
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported - by using `__import__,` like the example below
**1. My first toolbox!**

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
- Do not use the function `print` (with string format to display integers) more than 4 times
- You have to define:
	- the value `10` to a variable `a`
	- the value `5` to a variable `b`
	- and use those two variables only, as arguments when calling functions (including `print`)
- `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
- Your program should call each of the imported functions. See example below for format
- the word `calculator_1` should be used only once in your file
- You are not allowed to use `*` for importing or `__import__`
- Your code should not be executed when imported

* **2. How to make a script dynamic!**
  * [2-args.py](./2-args.py): Python program that prints the number of
  and list of its arguments.
  * Output: `[Number of arguments] argument` (if number is one) or `arguments` (otherwise), followed by:
    * `:` (or `.` if no argumets were passed), followed by
    * A new line, followed by
    * One argument per line - the position of the argument (starting at `1`) followed by `:` followed by the argument value and another new line.

* **3. Infinite addition**
  * [3-infinite_add.py](./3-infinite_add.py): Python program that prints the result of the
  addition of all arguments.
  * Output: Sum of the arguments followed by a new line.

* **4. Who are you?**
  * [4-hidden_discovery.py](./4-hidden_discovery.py): Python program that prints all the
  names defined by the compiled module `hidden_4.pyc`.
  * Output: One name per line in alphabetical order.
  * Names starting with `__` are not printed.

* **5. Everything can be imported**
  * [5-variable_load.py](./5-variable_load.py): Python program that imorts the
  variable `a` from the file [variable_load_5.py](./variable_load_5.py) and prints its value.

* **6. Build my own calculator!**
  * [100-my_calculator.py](./100-my_calculator.py): Python program that imports all functions
  from the file [calculator_1.py](./calculator_1.py) and handles basic operations.
  * Usage: `./100-my_calculator.py <a> <operator> <b>` followed by a new line.
  * Output: `<a> <operator> <b> = <result>` followed by a new line.
  * The parameter `operator` can be:
    * `+` for addition
    * `-` for subtraction
    * `*` for multiplication
    * `/` for division
  * If the operator is none of the above, the function prints `Unknown operator.
  Available operators: +, -, *, and /` followed by a new line and exits
  with a status value of `1`.
  * If the number of arguments is not three, the program prints `Usage: ./100-my_calculator.py <a> <operator> <b>` followed by a new line and exits with a status value of `1`.

* **7. Easy print**
  * [101-easy_print.py](./101-easy_print.py): Python program that prints
  `#pythoniscool` followed by a new line in the standard output.
  * Without using `print`, `eval`, `open`, or `sys`.

* **8. ByteCode -> Python #3**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode provided by Holberton School.

* **9. Fast alphabet**
  * [103-fast_alphabet.py](./103-fast_alphabet.py): Python program that prints the alphabet in
  uppercase, followed by a new line.
  * Without using loops, conditoinals, `str.join()`, string literals, or system calls.

