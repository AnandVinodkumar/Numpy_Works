import numpy

numbers1 = [1,2,3,4]
numbers2 = [5,6,7,8]

# list

array1 = numpy.array(numbers1)
array2 = numpy.array(numbers2)
print(array1 * array2)  # Vectorized operation

# Display addition, subtraction, multiplication, and division of two arrays

print("Addition: ", array1 + array2)
print("Subtraction: ", array1 - array2)
print("Multiplication: ", array1 * array2)
print("Division: ", array1 / array2)