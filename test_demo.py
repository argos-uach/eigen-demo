import demo 
import numpy as np
def test_multiplyby2():
    A=[[1., 2.],[3.,4.]]
    L=np.array(A, dtype=np.float32)

    x = demo.multMatrix(m=L)
    
    np.testing.assert_allclose(x,2*L, rtol=1e-07, atol=0, equal_nan=True, err_msg='', verbose=True)

