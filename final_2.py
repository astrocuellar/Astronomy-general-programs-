import numpy as np
import VoigtFit



z_DLA = 2.8926
logNHI = 20.5, 0.11		# value, uncertainty
dataset = VoigtFit.DataSet(z_DLA)

UVB_fname = 'J1358_norm_UV.dat'
res_UVB = 5500
wl_uvb, spec_uvb, err_uvb = np.loadtxt(UVB_fname, unpack=True)
dataset.add_data(wl_uvb, spec_uvb, 299792./res_UVB, err=err_uvb, normalized=True)

VIS_fname = 'J1358_norm_VIS.dat'
res_VIS = 8900
wl_VIS, spec_VIS, err_VIS = np.loadtxt(VIS_fname, unpack=True)
dataset.add_data(wl_VIS, spec_VIS, 299792./res_VIS, err=err_VIS, normalized=True)






# AlIII:
dataset.reset_components()
dataset.add_line('SiIV_1393', velspan=(-1200, 500))
dataset.add_line('SiIV_1402', velspan=(-1200, 500))
dataset.add_line('NV_1238', velspan=(-1200, 500))
dataset.add_line('NV_1242', velspan=(-1200, 500))

# dataset.interactive_components('SiIV_1393')
# dataset.interactive_components('SiIV_1402')







name_final = 'test_4'


dataset.add_component_velocity('NV',  +210.0   , 53.7 ,  14.07  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',   +57.7   , 78.9 ,  14.62  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',   -23.1   , 19.3 ,  13.10  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -610.3   , 35.4 ,  15.44  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -934.0   , 80.1 ,  14.14  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -477.6   , 24.5 ,  14.99  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -717.7   , 69.5 ,  14.53  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -376.1   , 73.6 ,  14.24  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -163.0   , 67.5 ,  14.68  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV',  -567.2   , 26.3 ,  14.72  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV', -1062.0   , 96.9 ,  13.78  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV', -291.0   , 20.9 ,  13.78  ,  var_z=False, var_b=True)
dataset.add_component_velocity('NV', -81.0    , 10.9 ,  13.78  ,  var_z=False, var_b=True)



dataset.add_component_velocity('SiIV',  +199.7  ,  78.6 ,  13.38,   var_z=True, var_b=True  , tie_z='z0_NV', tie_b='b0_NV')
dataset.add_component_velocity('SiIV',   +48.6  ,  66.4 ,  14.41,   var_z=True, var_b=True  , tie_z='z1_NV', tie_b='b1_NV')
dataset.add_component_velocity('SiIV',   -25.0  ,  21.9 ,  15.28,   var_z=True, var_b=True  , tie_z='z2_NV', tie_b='b2_NV')
dataset.add_component_velocity('SiIV',  -603.1  ,  52.5 ,  12.90,   var_z=True, var_b=True  , tie_z='z3_NV', tie_b='b3_NV')
dataset.add_component_velocity('SiIV',  -952.4  , 126.0 ,  12.21,   var_z=True, var_b=True  , tie_z='z4_NV', tie_b='b4_NV')
dataset.add_component_velocity('SiIV',  -952.4  , 126.0 ,  12.71,   var_z=True, var_b=True  , tie_z='z5_NV', tie_b='b5_NV')
# dataset.add_component_velocity('SiIV',  -952.4  , 126.0 ,  12.06,   var_z=True, var_b=True  , tie_z='z7_NV', tie_b='b7_NV')
# dataset.add_component_velocity('SiIV',  -952.4  , 126.0 ,  11.12,   var_z=True, var_b=True  , tie_z='z8_NV', tie_b='b8_NV')





# dataset.add_line('NV_1238', velspan=(-1200, 500))
# dataset.add_line('NV_1242', velspan=(-1200, 500))






# Crucial step:
dataset.prepare_dataset()
popt, chi2 = dataset.fit()

# dataset.PLot_fit(max_rows=4, filename='test_3')



# print('Best fits:')






# dataset.save_parameters(name_final)
# #
# if logNHI:
#     dataset.print_metallicity(*logNHI)
# dataset.print_total()

# # dataset.save_fit_regions('region')
# dataset.PLot_fit(individual=True)  # con PL en mayuscula es para plotear en el orden que yo quiero


dataset.PLot_fit_2(max_rows=2, filename='NV_SiIV_J1358_plot')