import os
import re
import sys

sys.path.append("/Users/cmcneile/projects/qed/pythonlib")
import util
nt = 8 

print("Getting fine pion correlators")
wdir_fine = "corr"
file_tag = "corr_fine_latt_"
#corr_tag =  "pion_w_w_d_d_m0.001524_q-.2_m0.001524_q-.2_p000"
corr_l = [  "pion_w_w_d_d_m0.001524_q-.2_m0.001524_q-.2_p000" ,"pion_w_w_d_d_m0.003328_q-0.1_m0.003328_q-0.1_p000" ,"pion_w_w_d_d_m0.0673_q-0.1_m0.0673_q-0.1_p000"    ]  
mass_l = [ 0.001524 , 0.003328 , 0.0673 ] 

##otag= "pion_fine"


cfglist_fine =  util.get_config_list_tag(wdir_fine, file_tag) 
print("INFO Number of fine correlators ",  len(cfglist_fine) )

#for cfg in cfglist_fine :
#  print(cfg)

##sys.exit(0)
##massl = [0.001524, 0.003328, 0.0673 ] 

util.write_corr_csv(cfglist_fine, wdir_fine, corr_l[0], file_tag, nt ) 
for corr_tag in corr_l[1:] :
   util.write_corr_csv(cfglist_fine, wdir_fine, corr_tag, file_tag, nt, True ) 

##sys.exit(0)


#
#  --------------------------------------------------
#
print("Getting sloppy pion correlators")


wdir_coarse = "corr"
file_tag = "corr_loose_latt_"

t_list = [0 , 1, 2 ,3, 4 , 5,  6 , 7] 
##t_list = [ ]

cfglist_coarse =  util.get_config_list_tag(wdir_coarse, file_tag) 
print("INFO Number of coarse correlators ",  len(cfglist_coarse) )

util.write_corr_many_csv(cfglist_coarse, wdir_coarse, corr_l[0], file_tag, t_list, nt, False ) 
for corr_tag in corr_l[1:] :
  util.write_corr_many_csv(cfglist_coarse, wdir_coarse, corr_tag, file_tag, t_list, nt, True ) 

