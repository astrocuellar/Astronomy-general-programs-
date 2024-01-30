# Uso de voigt profile:

import numpy as np
import VoigtFit

z_DLA = 2.8926
logNHI = 20.5, 0.11		# value, uncertainty

name_final = 'nombre_output'



dataset = VoigtFit.DataSet(z_DLA)

UVB_fname = 'J1358_norm_UV.dat'
res_UVB = 5500
wl_uvb, spec_uvb, err_uvb = np.loadtxt(UVB_fname, unpack=True)
dataset.add_data(wl_uvb, spec_uvb, 299792./res_UVB, err=err_uvb, normalized=True)

VIS_fname = 'J1358_norm_VIS.dat'
res_VIS = 8900
wl_VIS, spec_VIS, err_VIS = np.loadtxt(VIS_fname, unpack=True)
dataset.add_data(wl_VIS, spec_VIS, 299792./res_VIS, err=err_VIS, normalized=True)



# IONES:
dataset.reset_components()
dataset.add_line('SiIV_1393', velspan=(-1200, 500))
dataset.add_line('SiIV_1402', velspan=(-1200, 500))
dataset.add_line('NV_1238', velspan=(-1200, 500))
dataset.add_line('NV_1242', velspan=(-1200, 500))




dataset.add_component_velocity('NV',  +210.0   , 53.7 ,  14.07  ,  var_z=False, var_b=True)
dataset.add_component_velocity('SiIV',  +199.7  ,  78.6 ,  13.38,   var_z=True, var_b=True  , tie_z='z0_NV', tie_b='b0_NV')




# Crucial step:
dataset.prepare_dataset()
popt, chi2 = dataset.fit()

print('Best fits:')
dataset.save_parameters(name_final)
dataset.print_total()
dataset.save_fit_regions('region')
dataset.PLot_fit(individual=True)  # con PL en mayuscula es para plotear en el orden que yo quiero
