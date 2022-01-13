import demo 
import numpy as np
import pickle

diccionarioNumpy={}
diccionarioEigen={}
for i in range(100,1001,10):
    A=np.random.randn(i,i)
    B=np.random.randn(i,i)
    time_obj_Numpy = %timeit -r10 -n5 -o np.dot(A,B)
    diccionarioNumpy[i]=time_obj_Numpy.average

    A1=np.random.randn(i,i)
    A1= A1.astype(np.float32, order="F")
    B1=np.random.randn(i,i)
    B1 = B1.astype(np.float32, order="F")
    time_obj_Eigen = %timeit -r10 -n5 -o demo.multMatrixByMatrix_Ref(matriz1=A1, matriz2=B1)
    diccionarioEigen[i]=time_obj_Eigen.average
with open("profiling_np_dot", "wb") as f:
    pickle.dump(time_obj_Numpy, f)
    time_obj_NumpyRecuperado=pickle.load(f)
with open("profiling_eigen", "wb") as c:
    pickle.dump(time_obj_Eigen, c)
    time_obj_EigenRecuperado=pickle.load(f)