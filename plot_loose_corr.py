import pandas  as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("/Users/cmcneile/projects/qed/pythonlib")
import pcorr

name = "corr_loose_latt_.csv"
nt = 8
corr_tag = "pion_w_w_d_d_m0.001524_q-.2_m0.001524_q-.2_p000"
##corr_tag = "pion_w_w_d_d_m0.0673_q-0.1_m0.0673_q-0.1_p000"

df, qmass = pcorr.load_corr(name,corr_tag)

#  t_source = 0
df_t0 = df[df["tsrc"] == 0  ].copy()
df_t0.drop(["tsrc"], inplace=True, axis=1)


t_av = [ 0 , 1,2 ,3 ,4 ] 
df_av = pcorr.average_source(df , t_av)

#
#  precise analysis
#
name_p = "corr_fine_latt_.csv"
df_p, qmass_p = pcorr.load_corr(name_p,corr_tag)
print("Precise time sources = " , df_p["tsrc"].unique())
df_p.drop(["tsrc"], inplace=True, axis=1)



#
#
#

##  --------------------------------------------------

ttt  = dict()
corr      = dict()
corr_err  = dict()

ttt["t0"],corr["t0"],corr_err["t0"] = pcorr.get_mean_corr(df_t0,nt,0.05)
ttt["av"],corr["av"],corr_err["av"] = pcorr.get_mean_corr(df_av,nt)

ttt["t_prec"],corr["t_prec"],corr_err["t_prec"] = pcorr.get_mean_corr(df_p,nt,-0.05)


##
##  plot
##

do_plot = lambda tag__, mk, lab : plt.errorbar(ttt[tag__],corr[tag__],corr_err[tag__], fmt=mk , label=lab)

do_plot("av", "go", "(sloppy) tsrc=t_av") 
do_plot("t0", "ro", "(sloppy)tsrc=0") 
do_plot("t_prec", "bo", "(precise)tsrc=7") 

plt.title("Pseudoscalar correlator at quark mass = " + str(qmass) )
plt.legend()

plt.xlabel('t')
plt.ylabel(r'corr(t)')
plt.xlim(0,4.2)


##plt.savefig("pioncorr.png")

plt.show()
