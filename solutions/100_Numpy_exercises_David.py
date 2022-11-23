#!/usr/bin/env python
# coding: utf-8

# # 100 numpy exercises
# 
# This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
# and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
# and new users but also to provide a set of exercises for those who teach.
# 
# 
# If you find an error or think you've a better way to solve some of them, feel
# free to open an issue at <https://github.com/rougier/numpy-100>.

# File automatically generated. See the documentation to update questions/answers/hints programmatically.

# Run the `initialize.py` module, then for each question you can query the
# answer or an hint with `hint(n)` or `answer(n)` for `n` question number.

# In[ ]:


get_ipython().run_line_magic('run', 'initialise.py')


# #### 1. Import the numpy package under the name `np` (★☆☆)

# In[1]:


import numpy as np


# #### 2. Print the numpy version and the configuration (★☆☆)

# In[9]:


print(np.__version__)
np.show_config()


# #### 3. Create a null vector of size 10 (★☆☆)

# In[10]:


np.zeros(10)


# #### 4. How to find the memory size of any array (★☆☆)

# In[15]:


x = np.array([1,2,3])
print("Memory size of numpy array:", x.size * x.itemsize)


# #### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)

# In[18]:


np.info(np.add)


# #### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)

# In[21]:


np.where(np.arange(10)==4,1,0)


# #### 7. Create a vector with values ranging from 10 to 49 (★☆☆)

# In[23]:


np.arange(10,49)


# #### 8. Reverse a vector (first element becomes last) (★☆☆)

# In[30]:


np.flip(np.arange(5))


# #### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)

# In[37]:


np.arange(9).reshape((3,3))


# #### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)

# In[44]:


x = np.array([1,2,0,0,4,0])
np.nonzero(x)


# #### 11. Create a 3x3 identity matrix (★☆☆)

# In[47]:


np.identity(3)


# #### 12. Create a 3x3x3 array with random values (★☆☆)

# In[51]:


np.random.rand(3,3,3)


# #### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

# In[59]:


x = np.random.rand(10,10)
print(x)
print(x.min())
print(x.max())


# #### 14. Create a random vector of size 30 and find the mean value (★☆☆)

# In[60]:


np.mean(np.random.rand(30))


# #### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)

# In[67]:


x = np.ones((4,4))
x[1:-1,1:-1] = 0
x


# #### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)

# In[73]:


np.pad(np.ones((4,4)), pad_width=1, mode='constant', constant_values=0)


# #### 17. What is the result of the following expression? (★☆☆)
# ```python
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
# 0.3 == 3 * 0.1
# ```

# In[76]:


print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)


# #### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)

# In[88]:


np.diag(1 + np.arange(4),k=-1)


# #### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)

# In[115]:


x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# #### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)

# In[122]:


print(np.unravel_index(99,(6,7,8)))


# #### 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)

# In[128]:


np.tile(np.array([[0,1],[1,0]]),(4,4))


# #### 22. Normalize a 5x5 random matrix (★☆☆)

# In[131]:


x = np.random.rand(5,5)
x = (x - np.mean(x))/np.std(x)
x


# #### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)

# In[ ]:


= np.dtype([("r", np.ubyte, 1),
                 ("g", np.ubyte, 1),
                 ("b", np.ubyte, 1),
                 ("a", np.ubyte, 1)])


# #### 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)

# In[133]:


x = np.random.rand(5,3)
y = np.random.rand(3,2)
z = np.dot(x,y)
z


# #### 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)

# In[142]:


x = np.arange(9)
x[(3 < x) & (x < 8)] *= -1
x


# #### 26. What is the output of the following script? (★☆☆)
# ```python
# # Author: Jake VanderPlas
# 
# print(sum(range(5),-1))
# from numpy import *
# print(sum(range(5),-1))
# ```

# In[155]:


print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


# #### 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
# ```python
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z
# ```

# In[164]:


Z = np.array([1,2])
Z**Z
Z <- Z
1j*Z
Z/1/1


# #### 28. What are the result of the following expressions? (★☆☆)
# ```python
# np.array(0) / np.array(0)
# np.array(0) // np.array(0)
# np.array([np.nan]).astype(int).astype(float)
# ```

# In[172]:


print(np.array(0) / np.array(0))
print(np.array(0) // np.array(0))
print(np.array([np.nan]).astype(int).astype(float))


# #### 29. How to round away from zero a float array ? (★☆☆)

# In[208]:


Z = np.random.uniform(-10,+10,20)
print(np.copysign(np.ceil(np.abs(Z)), Z))


# #### 30. How to find common values between two arrays? (★☆☆)

# In[174]:


a = np.array([1,2,3,4,5])
b = np.array([6,5,4,3,20])
print(np.intersect1d(a, b))


# #### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)

# In[215]:


defaults = np.seterr(all="ignore")
Z = np.ones(1) / 0
Z


# #### 32. Is the following expressions true? (★☆☆)
# ```python
# np.sqrt(-1) == np.emath.sqrt(-1)
# ```

# In[179]:


np.sqrt(-1) == np.emath.sqrt(-1)


# #### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)

# In[226]:


print(np.datetime64('today', 'D'))
print(np.datetime64('today', 'D') - np.timedelta64(1, 'D'))
print(np.datetime64('today', 'D') + np.timedelta64(1, 'D'))


# #### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)

# In[228]:


x = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(x)


# #### 35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)

# In[236]:


A = np.ones(3)
B = np.ones(3)
print(np.dot(A+B, -A/2))


# #### 36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)

# In[286]:


Z = np.random.uniform(0,10,10)
print(Z - Z%1)
print(np.ceil(Z))
print(np.floor(Z))
print(Z.astype(int))
print(np.trunc(Z))


# #### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)

# In[284]:


Z = np.tile(np.arange(0, 5), (5,1))
print(Z)


# #### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)

# In[290]:


def generator():
    for i in range(10):
        yield i
        
np.fromiter(generator(), int, count=- 1)


# #### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)

# In[293]:


np.linspace(0,1,11, endpoint=False)[1:]


# #### 40. Create a random vector of size 10 and sort it (★★☆)

# In[282]:


np.sort(np.random.rand(10))


# #### 41. How to sum a small array faster than np.sum? (★★☆)

# In[294]:


x = np.arange(10)
np.add.reduce(x)


# #### 42. Consider two random array A and B, check if they are equal (★★☆)

# In[299]:


A = np.ones((5,5))
B = np.ones((5,5))
np.array_equal(A,B)


# #### 43. Make an array immutable (read-only) (★★☆)

# In[303]:


a = np.arange(10)
a.setflags(write=False)
a[0] = 1


# #### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)

# In[308]:


z= np.random.random((10,2))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)


# #### 45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)

# In[283]:


x = np.random.rand(10)
print(x)
x[np.argmax(x)] = 0
print(x)


# #### 46. Create a structured array with `x` and `y` coordinates covering the [0,1]x[0,1] area (★★☆)

# In[338]:


X = np.zeros((5,5), [('x',float),('y',float)])
X['x'], X['y'] = np.meshgrid(np.linspace(0,1,5),
                             np.linspace(0,1,5))
print(X)


# #### 47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)

# In[337]:


X = np.arange(8)
Y = np.random.rand(5)
C = 1.0 / np.subtract.outer(X, Y)
C


# #### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)

# In[340]:


for dtype in [np.int8, np.int32, np.int64]:
    print(np.iinfo(dtype).min)
    print(np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print(np.finfo(dtype).min)
    print(np.finfo(dtype).max)
    print(np.finfo(dtype).eps)


# #### 49. How to print all the values of an array? (★★☆)

# In[347]:


x = np.random.rand(5)
print(x)
#?


# #### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)

# In[344]:


value=10
x = np.linspace(-100,100, 10)
print(x)
x[np.argmin(np.abs(x - 10))]


# #### 51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)

# In[ ]:





# #### 52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)

# In[ ]:





# #### 53. How to convert a float (32 bits) array into an integer (32 bits) in place?

# In[ ]:





# #### 54. How to read the following file? (★★☆)
# ```
# 1, 2, 3, 4, 5
# 6,  ,  , 7, 8
#  ,  , 9,10,11
# ```

# In[ ]:





# #### 55. What is the equivalent of enumerate for numpy arrays? (★★☆)

# In[ ]:





# #### 56. Generate a generic 2D Gaussian-like array (★★☆)

# In[ ]:





# #### 57. How to randomly place p elements in a 2D array? (★★☆)

# In[ ]:





# #### 58. Subtract the mean of each row of a matrix (★★☆)

# In[ ]:





# #### 59. How to sort an array by the nth column? (★★☆)

# In[ ]:





# #### 60. How to tell if a given 2D array has null columns? (★★☆)

# In[ ]:





# #### 61. Find the nearest value from a given value in an array (★★☆)

# In[ ]:





# #### 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)

# In[ ]:





# #### 63. Create an array class that has a name attribute (★★☆)

# In[ ]:





# #### 64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)

# In[ ]:





# #### 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)

# In[ ]:





# #### 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)

# In[ ]:





# #### 67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)

# In[ ]:





# #### 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset  indices? (★★★)

# In[ ]:





# #### 69. How to get the diagonal of a dot product? (★★★)

# In[ ]:





# #### 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)

# In[ ]:





# #### 71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)

# In[ ]:





# #### 72. How to swap two rows of an array? (★★★)

# In[ ]:





# #### 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the  triangles (★★★)

# In[ ]:





# #### 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)

# In[ ]:





# #### 75. How to compute averages using a sliding window over an array? (★★★)

# In[ ]:





# #### 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is  shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)

# In[ ]:





# #### 77. How to negate a boolean, or to change the sign of a float inplace? (★★★)

# In[ ]:





# #### 78. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to compute distance from p to each line i (P0[i],P1[i])? (★★★)

# In[ ]:





# #### 79. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P, how to compute distance from each point j (P[j]) to each line i (P0[i],P1[i])? (★★★)

# In[ ]:





# #### 80. Consider an arbitrary array, write a function that extract a subpart with a fixed shape and centered on a given element (pad with a `fill` value when necessary) (★★★)

# In[ ]:





# #### 81. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]? (★★★)

# In[ ]:





# #### 82. Compute a matrix rank (★★★)

# In[ ]:





# #### 83. How to find the most frequent value in an array?

# In[ ]:





# #### 84. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★)

# In[ ]:





# #### 85. Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★)

# In[ ]:





# #### 86. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1). How to compute the sum of of the p matrix products at once? (result has shape (n,1)) (★★★)

# In[ ]:





# #### 87. Consider a 16x16 array, how to get the block-sum (block size is 4x4)? (★★★)

# In[ ]:





# #### 88. How to implement the Game of Life using numpy arrays? (★★★)

# In[ ]:





# #### 89. How to get the n largest values of an array (★★★)

# In[ ]:





# #### 90. Given an arbitrary number of vectors, build the cartesian product (every combinations of every item) (★★★)

# In[ ]:





# #### 91. How to create a record array from a regular array? (★★★)

# In[ ]:





# #### 92. Consider a large vector Z, compute Z to the power of 3 using 3 different methods (★★★)

# In[ ]:





# #### 93. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A that contain elements of each row of B regardless of the order of the elements in B? (★★★)

# In[ ]:





# #### 94. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★)

# In[ ]:





# #### 95. Convert a vector of ints into a matrix binary representation (★★★)

# In[ ]:





# #### 96. Given a two dimensional array, how to extract unique rows? (★★★)

# In[ ]:





# #### 97. Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function (★★★)

# In[ ]:





# #### 98. Considering a path described by two vectors (X,Y), how to sample it using equidistant samples (★★★)?

# In[ ]:





# #### 99. Given an integer n and a 2D array X, select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees, i.e., the rows which only contain integers and which sum to n. (★★★)

# In[ ]:





# #### 100. Compute bootstrapped 95% confidence intervals for the mean of a 1D array X (i.e., resample the elements of an array with replacement N times, compute the mean of each sample, and then compute percentiles over the means). (★★★)

# In[ ]:




