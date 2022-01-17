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

def unpack_results(results):
    x = list(results.keys())
    y = [timeit.average for timeit in results.values()]
    yerr = [timeit.stdev for timeit in results.values()]
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
ax.set_title('Openblas Pablo H')

# %%
