
Basic Arithmetic operations class for python
=======================

Overview
----------
A python class **(math_lib)** for basic arithmetic operations.
The class can be used for addition, subtraction, multiplication and division.

The class works with **integer** number.

Operations:
---------
 - Addition **(+)**
 - Subtraction **(-)**
 - Multiplication **( * )**
 - Division **(/)**
 
|Operation  | Description                 | Example     | Results     |
|:----------: | :--------------------------:  | :------------:| :------------:|
|    +      | addition             | 1 + 2 = 3   | integer |
|    −      | subtraction         | 5 - 1 = 4   | integer |
|    *      | multiplication      | 2 * 9 = 18  | integer|
|    ÷      | division          | 9 / 2 = 4.5 | double|

Usage
---------------------

```python
# import MyMath from math_lib module

from math_lib import MyMath
self.MyMath = MyMath()

# Аddition of two numbers.
print MyMath.addition_two_numbers(1, 2)

# Subtraction of two numbers.
print MyMath.subtraction_two_numbers(5, 1)

# Multiplication of two numbers.
print MyMath.multiplication_two_numbers(2, 9)

# Division of two numbers.
print MyMath.division_two_numbers(9, 2) 
```  

Test
---------------------
``` powershell
$ py tests.py -v

.py
....................................
Ran 36 tests in 0.003s

OK
```
