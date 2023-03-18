# 0x00. Python - Hello, World
**0. Run Python file**

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

```
guillaume@ubuntu:~/py/0x00$ cat main.py
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$
```
**1. Run inline**

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`

**2. Hello, print**

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# chmod u+x 2-print.py
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ls
0-run  1-run_inline  2-print.py  lists.h  README.md
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./2-print.py
"Programming is like building a multilingual puzzle
```
**3. Print integer**

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "source code") in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py "here")
- The output of the script should be:
	- the number, followed by `Battery street`,
	- followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/ "tips")

```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./3-print_number.py
98 Battery street
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**4. Print float**

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py "here")
- The output of the program should be:
	- `Float:`, followed by the float with only 2 digits
	- followed by a new line
- You are not allowed to cast `number` to string
- You have to use f-strings

```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./4-print_float.py
Float: 3.14
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**5. Print string**

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py "source code") in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py "here") 
- The output of the program should be:
	- 3 times the value of `str`
	- followed by a new line
	- followed by the 9 first characters of `str`
	- followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**6. Play with strings**

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py "source code") to print `Welcome to Holberton School!`

- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py "here")
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./6-concat.py
Welcome to Holberton School!
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**7. Copy - Cut - Paste**

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py "source code")
- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py "here")
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```
**8. Create a new sentence**

Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py "source code") to print `object-oriented programming with Python`, followed by a new line.
- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py "here")
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./8-concat_edges.py
object-oriented programming with Python
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**9. Easter Egg**

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# wc -m 9-easter_egg.py
31 9-easter_egg.py
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**10. Linked list cycle**

#### Technical interview preparation:
- You are not allowed to google anything
- Whiteboard first
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.
- Prototype: `int check_cycle(listint_t *list);`
- Return: `0` if there is no cycle, `1` if there is a cycle

Requirements:
- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# gcc 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./cycle
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**11. Hello, write**

Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
- Use the function `write` from the `sys` module
- You are not allowed to use `print`
- Your script should print to `stderr`
- Your script should exit with the status code `1`
```
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# echo $
$
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# ./100-write.py 2> q
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world# cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
root@c54b1b2b8256:/alx-higher_level_programming/0x00-python-hello_world#
```
**12. Compile**

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable `$PYFILE`

The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

