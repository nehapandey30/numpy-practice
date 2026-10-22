import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([3,2,4,6])
combine=np.concatenate((arr1,arr2))
print(combine)
# arraay compatibility

print("compatibility shapes", arr1.shape==arr2.shape)
# adding new roe in present array
original=np.array([[1,2],[2,3],[4,5]])
new_row=np.array([[5,6]])
with_new_row=np.vstack((original,new_row))
print(original)
print(with_new_row)
new_col=np.array([[7],[8],[9]])
with_new_col=np.hstack((original,new_col))
print("new column data ",with_new_col)


# deletion

array=np.array([1,2,4,5,7,8,8,9,7,5,4,2])
delete=np.delete(array,2)
print("array after deleted",delete)


