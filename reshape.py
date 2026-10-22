import numpy as np
arr1=np.array([1,2,3,4,4,5,6,7,8,9,9,10])
print("original array :",arr1)
arr2=arr1.reshape(3,4)
print("reshaped array",arr2)
flattend=arr2.flatten()
print("flattend array  is: ",flattend)
# ravel (returns view insted of copy) 
raveled=arr2.ravel()
print("raveled array  is: ",raveled)
# transpose 
transpose=arr2.T
print("transposed array is: ",transpose)
