
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
|    +      | addition             | 2 + 7 = 9   | integer |
|    −      | subtraction         | 9 - 2 = 7   | integer |
|    *      | multiplication      | 2 * 7 = 14  | integer|
|    ÷      | division          | 9 / 2 = 4.5 | double|

Usage
---------------------

<pre>
# import MyMath from math_lib module

from math_lib import MyMath
self.MyMath = MyMath()

# add 2 and 7
print my_math.add(2, 7)

# subtract 9 from 2
print my_math.sub(9, 2)

# multiply 2 by 7
print my_math.mul(2, 7)

# divide 9 by 2
print operation.div(9, 2)   
</pre>

Test
---------------------
<pre>
$ py tests.py -v

WIP

OK
</pre>