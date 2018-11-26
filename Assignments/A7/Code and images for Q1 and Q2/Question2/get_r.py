import numpy as np
    
def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    if 0 < alpha < 1 and 0 <= delta < 1 and Z > 0:
        if np.isscalar(K) and np.isscalar(L):
            if K > 0 and L > 0:
                r = alpha * Z * (L / K) ** (1 - alpha) - delta
                return r
            
        elif not np.isscalar(K) and not np.isscalar(L) and K.shape == L.shape:
            if all(K > 0) and all(L > 0):
                r = alpha * Z * (L / K) ** (1 - alpha) - delta
                return r
    return None                    
                
    

   


