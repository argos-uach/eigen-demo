import demo 
import numpy as np
import pickle
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

diccionarioNumpy={}
diccionarioEigen={}
for i in [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]:
    A=np.random.randn(i, i).astype('float32')
    B=np.random.randn(i, i).astype('float32')
    time_obj_Numpy = %timeit -r5 -n5 -q -o np.dot(A,B)
    diccionarioNumpy[i] = time_obj_Numpy
    A1 = np.asfortranarray(A)
    B1 = np.asfortranarray(B)
    time_obj_Eigen = %timeit -r5 -n5 -q -o demo.multMatrixByMatrix_Ref(matriz1=A1, matriz2=B1)
    diccionarioEigen[i] = time_obj_Eigen

with open("profiling_np_dot.pkl", "wb") as f:
    pickle.dump(diccionarioNumpy, f)
    
with open("profiling_eigen.pkl", "wb") as c:
    pickle.dump(diccionarioEigen, c)
    