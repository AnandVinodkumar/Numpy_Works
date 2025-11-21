# numpy
# ========================
# pip install numpy >> Install numpy package
# pip list >> List all packages

import numpy

# elements = [1, 2, 3, 4, 5]

# array = numpy.array(elements)   # Convert list to numpy array

# print(array)    # Output: [1 2 3 4 5]

# print(array[1])  # Output: 2 (Accessing second element)

# print(type(array))  # Output: <class 'numpy.ndarray'>

# Create an array of numbers from num1 to num2 should be entered by user
num1 = int(input("Enter starting number: "))

num2 = int(input("Enter ending number: "))

elements = list(range(num1, num2 + 1))

array = numpy.array(elements)

print(array)


"""
Numpy (Numerical Python) 
Its a third party package built using C language

It has array which is faster than list
                    a)No need of loops in array as it is faster than list
                    b)Arrays are homogeneous
                    c)So many built-in functions (mean, median, mode..)
                    d)Array operations and matrix operations

arrays are better to perform fourier transform, linear algebra, random number capabilities

array = [1,2,3,4]
array2 = [5,6,7,8]
print(array * array2)  # Output: [ 5 12 21 32] (Vectorized operation not possible in lists)  


"""