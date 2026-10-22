import numpy as np
vector1=np.array([1,2,3,4,5])
vector2=np.array([1,5,7,8,9])
print("vector is : ",vector1)
# operations
print("vector addition",vector1+vector2)
print("vector multiplictaion",vector1*vector2)

print("vector dot product",np.dot(vector1,vector2))
angle=np.arccos(np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2)))

print(angle)

