import numpy as np
import VoigtFit


def crear_complexes(C4, nube, ion):
    val = []
    e_val = []
    for i in range(len(nube)):
        v = nube[i]
        val.append(C4[v][0])
        e_val.append(C4[v][1])
    logN_pdf = [np.random.normal(n, e, 10000)
                for n, e in zip(val, e_val)]
    logsum = np.log10(np.sum(10**np.array(logN_pdf), 0))
    e_logsum = np.std(logsum)
    total_logN = np.median(logsum)
    print( ion , ' = [', str(round(total_logN, 2)) + ', ', str(round(e_logsum, 2)), ']')
    pass

def velocidad(vel, indices):
    val = []
    for i in range(len(indices)):
        v = indices[i]
        val.append(vel[v])
    media = np.mean(val)
    print(' velocidad = ', media)
    pass



def crear_complexes_print(C4, nube):
    val = []
    e_val = []
    for i in range(len(nube)):
        v = nube[i]
        val.append(C4[v][0])
        e_val.append(C4[v][1])
    logN_pdf = [np.random.normal(n, e, 10000)
                for n, e in zip(val, e_val)]
    logsum = np.log10(np.sum(10**np.array(logN_pdf), 0))
    e_logsum = np.std(logsum)
    total_logN = np.median(logsum)
    
    return str(round(total_logN, 2)), str(round(e_logsum, 2))
    




#J0015:
print('')
print('J0015:')
vel =  -153.3,-269.3,+7.1,-84.0,-487.2,-303.2,-210.3,+49.6


NV =  [14.079 , 0.036],[14.618 , 0.016],[12.978 , 0.360],      [15.456 , 0.311],[14.143 , 0.036],[14.994 , 0.127],      [14.532 , 0.020],[14.232 , 0.161],[14.664 , 0.017],      [14.724 , 0.175],[13.780 , 0.073],[13.713 , 0.180],[13.864 , 0.388]


SiIV = [13.364 ,0.048],[14.531 ,0.018],[15.285 ,1.504],       [12.966 ,0.059],[12.257 ,0.349],[12.728 ,0.090],       [0, 0],[0, 0],[0, 0],       [0, 0],[0, 0],[0, 0],[0, 0]


complex_high =  [3, 4, 5, 6, 7, 8, 9, 10, 11]
complex_low = [0, 1, 2, 12]
complex_total = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]












print(' Complex low ionization:')
crear_complexes(SiIV, complex_low, 'SiIV')
crear_complexes(NV, complex_low, 'NV')
print('')
print()
print('')

SiIV_low_val, SiIV_low_err = crear_complexes_print(SiIV, complex_low)
NV_low_val, NV_low_err = crear_complexes_print(NV, complex_low)

print('Low  & ' + SiIV_low_val + '  $\pm$   '+  SiIV_low_err + 
      ' & ' + NV_low_val + '  $\pm$   '+  NV_low_err)


print('')
print('')

print(' Complex new high ionization:')
crear_complexes(SiIV, complex_high, 'SiIV')
crear_complexes(NV, complex_high, 'NV')
print('')
print('')

SiIV_high_val, SiIV_high_err = crear_complexes_print(SiIV, complex_high)
NV_high_val, NV_high_err = crear_complexes_print(NV, complex_high)

print('High  & ' + SiIV_high_val + '  $\pm$   '+  SiIV_high_err + 
      ' & ' + NV_high_val + '  $\pm$   '+  NV_high_err)



print(' Complex new Total ionization:')
crear_complexes(NV, complex_total, 'NV')
crear_complexes(SiIV, complex_total, 'SiIV')
print('')
print('')

SiIV_total_val, SiIV_total_err = crear_complexes_print(SiIV, complex_total)
NV_total_val, NV_total_err = crear_complexes_print(NV, complex_total)

print('Total  & ' + SiIV_total_val + '  $\pm$   '+  SiIV_total_err + 
      ' & ' + NV_total_val + '  $\pm$   '+  NV_total_err)


print('')
print('')
