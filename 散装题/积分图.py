import numpy as np
x=np.array([[2,1,2,3,4,3],[3,2,1,2,2,3],[4,2,1,1,1,2]])

integral=np.zeros(x.shape)
h,w=integral.shape

for i in range(h):
    for j in range(w):
        integral[i][j]=np.sum(x[:i+1,:j+1])
print(integral)