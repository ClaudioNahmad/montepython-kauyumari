from __future__ import print_function
from __future__ import division
import sys, os
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
from getdist import plots, MCSamples
import getdist, IPython
import pylab as plt
#print('GetDist Version: %s, Matplotlib version: %s'%(getdist.__version__, plt.matplotlib.__version__))
#matplotlib 2 doesn't seem to work well without usetex on
plt.rcParams['text.usetex']=True

#----------------------------------------------------------------------------------


g = plots.getSubplotPlotter(chain_dir=[u'/home/claudio/physics/01_montepython/montepython-kauyumari/chains/N1_nierika/bao_jla/nrk_12-1_cluster2_f1.7_CONVERGED/', '/home/claudio/physics/01_montepython/montepython-kauyumari/chains/N1_nierika/planck_bao_jla/nrk_12-1_cluster1_f1.7/'])
roots = ['2018-12-01_650000_','2018-12-01_800000_',]
params = [u'omega_b', u'omega_cdm', u'Omega_Lambda', u'b0_fld', u'b1_fld', u'H0']

param_3d = None
g.settings.alpha_filled_add=0.5

g.triangle_plot(roots, params, plot_3d_with_param=param_3d, filled=True, shaded=False
               ,legend_labels=[r'$w(N=1)$ BAO + JLA',r'$w(N=1)$ PlanckTT + lowP + BAO + JLA']
               ,legend_loc='upper right'
               ,line_args=[{'ls':'--', 'color':'green'},{'lw':1, 'color':'darkblue'}]
               ,contour_colors=['green','darkblue'])

g.export('prueba2_mp.pdf')
