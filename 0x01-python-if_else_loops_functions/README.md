# 0x01. Python - if/else, loops, functions
## Tasks
**0. Positive anything is better than negative nothing**

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py "here")
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
- The output of the program should be:
	- The number, followed by
		- if the number is greater than 0: `is positive`
		- if the number is 0: `is zero`
		- if the number is less than 0: `is negative`
	- followed by a new line
```
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
9 is positive
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
-5 is negative
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
-2 is negative
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
4 is positive
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
-1 is negative
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
-1 is negative
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
-4 is negative
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./0-positive_or_negative.py
5 is positive
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions#
```
**1. The last digit**

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py "here")
- The variable `number` will store a different value every time you will run this program
- You don’t have to understand what `import, random.randint` do. **Please do not touch this code.** This line should not change: `number = random.randint(-10000, 10000)`
- The output of the program should be:
	- The string `Last digit of`, followed by
	- the number, followed by
	- the string `is`, followed by the last digit of `number`, followed by
		- if the last digit is greater than 5: the string `and is greater than 5`
		- if the last digit is 0: the string `and is 0`
		- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
	- followed by a new line
```
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of 3836 is 6 and is greater than 5
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of -8439 is -9 and is less than 6 and not 0
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of 3957 is 7 and is greater than 5
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of 5221 is 1 and is less than 6 and not 0
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of -70 is 0 and is 0
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of -4532 is -2 and is less than 6 and not 0
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions# ./1-last_digit.py
Last digit of 1272 is 2 and is less than 6 and not 0
root@c54b1b2b8256:/alx-higher_level_programming/0x01-python-if_else_loops_functions#
```
**2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**

Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- You can only use one `print` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module
