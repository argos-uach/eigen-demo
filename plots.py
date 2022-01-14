#%%

%matplotlib inline 
import matplotlib.pyplot as plt
import numpy 
import pickle

with open("profiling_eigen", "rb") as f:
    result_eigen = pickle.load(f)

with open("profiling_np_dot", "rb") as f:
    result_numpy = pickle.load(f)
# %%

x = list(result_numpy.keys())
y = list(result_numpy.values())
fig, ax = plt.subplots(figsize=(5, 4), facecolor='w')
ax.plot(x, y, label='Numpy')
# ax.scatter(x, y)
y = list(result_eigen.values())
ax.plot(x, y, label='Eigen')
ax.set_xlabel('Tamaño de la matriz')
ax.set_ylabel('Tiempo promedio')
ax.legend()

# %%
