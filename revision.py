"""
Numpy
----------------------

list [1,2,3,4]

array [1 2 3 4] 1D
array [[1 2]
       [3 4]] 2D

array is homogeneous, all elements must be of the same type

vectorized operations >>> No loops needed

array can be used for huge data sets efficiently
"""

import numpy

n = numpy.array([[1, 2, 3, 4],[2,3,4,5]])

print(n)  # [[1 2 3 4]
          #  [2 3 4 5]]

print(n.reshape(4,2))  # [[1 2]
                       #  [3 4]
                       #  [2 3]
                       #  [4 5]]

# create a 3 x 4 matrix

n1 = numpy.random.randint(1,12, size=(3,4))

print(n1)

# create a 4 x 3 matrix having even numbers between 10 to 50

numpy.array([i for i in range(10,50,2)])

# or

numpy.array(list(range(10,50,2)))


# Create a 4 x 4 matrix using random numbers

n3 = numpy.random.randint(1,30,(4,4))
print(n3)

# create a 3,4 matrix and extract any submatrix from it

n4 = numpy.random.randint(1,30,(3,4))
print(n4)
print(n4[:2,:3])
print(n4.sum())
print(n4.mean())
print(n4.std())
print(numpy.mean(n4))
print(numpy.median(n4))
print(numpy.sum(n4))
print(numpy.std(n4))


# pandas
# ----------------------------
 
