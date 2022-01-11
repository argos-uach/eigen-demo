import demo 
import numpy as np

def test_multiplyby2_ref():
    A=[[1., 2.],[3.,4.]]
    L = np.array(A, dtype=np.float32, order="F")
    H = np.array(A, dtype=np.float32, order="F")

    demo.multMatrixRef(m=L)

    np.testing.assert_allclose(2*H, L, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)
