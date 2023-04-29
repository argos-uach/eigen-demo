#%%
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
    
# %%
%matplotlib inline 
import matplotlib.pyplot as plt
import pickle
import numpy as np

with open("profiling_eigen.pkl", "rb") as f:
    result_eigen = pickle.load(f)

with open("profiling_np_dot.pkl", "rb") as f:
    result_numpy = pickle.load(f)

def unpack_results(results):
    x = np.array(list(results.keys()))
    y = np.array([timeit.average for timeit in results.values()])
    yerr = np.array([timeit.stdev for timeit in results.values()])
    return x, y, yerr
    
x, y, yerr = unpack_results(result_numpy)
fig, ax = plt.subplots(figsize=(5, 4), facecolor='w')
ax.errorbar(x, y, yerr, label='Numpy')
# ax.scatter(x, y)
x, y, yerr = unpack_results(result_eigen)
ax.errorbar(x, y, yerr, label='Eigen')
ax.set_xlabel('Tamaño de la matriz')
ax.set_ylabel('Tiempo promedio')
ax.legend()
ax.set_title('MKL Pablo H')
ax.set_xscale('log')
ax.set_yscale('log')
# %%

# Speed-up
fig, ax = plt.subplots(figsize=(5, 4), facecolor='w')
x, y1, yerr1 = unpack_results(result_eigen)
x, y2, yerr2 = unpack_results(result_numpy)
ax.errorbar(x, y2/y1)
ax.set_xlabel('Tamaño de la matriz')
ax.set_xscale('log')
ax.set_ylabel('Speed up')

# %%
