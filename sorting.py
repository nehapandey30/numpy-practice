import numpy as np
unsort=np.array([1,2,7,8,4,63,2,4,6,7,8,0])
print("sorted array",np.sort(unsort))
twoDunsort=np.array([[5,4,3],[9,7,6],[6,0,2]])
print("sorted by column",np.sort(twoDunsort,axis=0))
print("sorted by column",np.sort(twoDunsort,axis=1))
print("sorted by column",np.sort(twoDunsort[:,1],axis=0))
