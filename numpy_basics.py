import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))


a = np.array(43)
b = np.array([3,2,5,1,5,6])
c = np.array([[1,2,3,4], [5,6,7,8]])
d = np.array([[[3,4,5], [1,2,3], [6,7,8]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



arr = np.array([1,2,3,4,5], ndmin = 5)

print(arr)
print('numbers of dimensions in array: ', arr.ndim)


arr = np.array([1,2,3,4,5])
print(arr[2] + arr[4])



arr = np.array([
    [1,2,3], 
    [4,5,6]
])
print("The first element of first row is: ", arr[0, 1])




arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[1:4])
print(arr[-3:])
arr_1 = np.arange(1,11)
print(arr_1)
arr_2 = np.arange(2,21,2)
print(arr_2)
arr_3 = np.linspace(0,10,5)
print(arr_3)
arr_4 = np.eye(3)
print(arr_4)
arr_5 = np.full(6,7)
print(arr_5)
arr_6 = np.zeros((2,4))
print(arr_6)


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(matrix[1,1])
print(matrix[2,2])
print(matrix[0:1])
print(matrix[2:3])
print(matrix[:,0])
print(matrix[:,1])
print(matrix[0:2,0:2])
print(matrix[1:3,1:3])

arr = np.arange(1, 13)
arr_1 = arr.reshape(3,4)
arr_2 = arr.reshape(2, 6)
arr_3 = arr.reshape(4, 3)
print(arr_1)
print()
print(arr_2)
print()
print(arr_3)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
arr_1 = arr.flatten()   # basically it creates the copy of the array
arr_2 = arr.ravel()
print(arr_1)
print(arr)         # see from this we can see that array didn't changed
print(arr_2)
print(arr)

