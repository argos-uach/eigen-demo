import demo 
import numpy as np
import pandas as pd

def test_multiplyby2_ref():
    df= pd.read_csv("out.csv")
    L = np.array(df.values, dtype=np.float32, order="F")
    H = np.array(df.values, dtype=np.float32, order="F")

    demo.multMatrixRef(m=L)

    np.testing.assert_allclose(2*H, L, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)
