import numpy as np
num=np.array([1,2,3,4,5,6,7,8,9,9])
even=num[num%2==0]
print(even)
#  filter with mask
mask=num>5
print("numbers greter than 5",num[mask])
# fancing indexing vs np.where()
