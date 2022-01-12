import demo 
import numpy as np
import pandas as pd

def test_multMatrixByMatrix_ref():
    df= pd.read_csv("out1.csv")
    dg= pd.read_csv("out2.csv")
    A1 = np.array(df.values, dtype=np.float32, order="F")
    A2 = np.array(df.values, dtype=np.float32, order="F")
    B1 = np.array(dg.values, dtype=np.float32, order="F")
    B2 = np.array(dg.values, dtype=np.float32, order="F")

    mult=demo.multMatrixByMatrix_Ref(matriz1=A1, matriz2=B1)

    np.testing.assert_allclose(np.dot(A2, B2.transpose()), mult, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)

