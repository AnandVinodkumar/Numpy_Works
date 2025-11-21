# 09-10-2025

import numpy

numbers = [[10,11,12,13],[14,15,16,17],[18,19,20,21],[22,23,24,25]]

n = numpy.array(numbers)

n[(n > 20)] = 0

print(n)