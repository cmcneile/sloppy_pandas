import pandas  as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("/Users/cmcneile/projects/qed/pythonlib")
import pcorr

name = "corr_loose_latt_.csv"
nt = 8
##corr_tag = "pion_w_w_d_d_m0.001524_q-.2_m0.001524_q-.2_p000"
corr_tag = "pion_w_w_d_d_m0.0673_q-0.1_m0.0673_q-0.1_p000"

df, qmass = pcorr.load_corr(name,corr_tag)

#  t_source = 0
df_t0 = df[df["tsrc"] == 0  ].copy()
df_t0.drop(["tsrc"], inplace=True, axis=1)


t_av = [ 0 , 1,2 ,3 ,4 ] 
df_av = pcorr.average_source(df , t_av)


#
#
#

##  --------------------------------------------------

ttt  = dict()
corr      = dict()
corr_err  = dict()

ttt["t0"],corr["t0"],corr_err["t0"] = pcorr.get_mean_corr(df_t0,nt)
ttt["av"],corr["av"],corr_err["av"] = pcorr.get_mean_corr(df_av,nt)

##
##  plot
##

do_plot = lambda tag__, mk, lab : plt.errorbar(ttt[tag__],corr[tag__],corr_err[tag__], fmt=mk , label=lab)

do_plot("av", "go", "tsrc=t_av") 
do_plot("t0", "ro", "tsrc=0") 

plt.title("Pseudoscalar correlator at quark mass = " + str(qmass) )
plt.legend()

plt.xlabel('t')
plt.ylabel(r'corr(t)')
plt.xlim(0,4.2)


##plt.savefig("pioncorr.png")

plt.show()
