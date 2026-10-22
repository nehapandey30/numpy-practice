import numpy as np
num=np.array([1,2,3,4,5,6,7,8,9,9])
indices=[0,2,4]
print(num[indices])
where_result=np.where(num>5)
print(where_result)
print("np where", num[where_result])
condition_array=np.where(num>5,"true","false")
print(condition_array)
