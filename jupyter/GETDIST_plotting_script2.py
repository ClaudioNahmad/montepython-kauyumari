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


g = plots.getSubplotPlotter(chain_dir=[u'/home/claudio/physics/01_montepython/montepython-kauyumari/chains/N2_nakawe/bao_jla/nkw_12-10_cluster1_f1.7/', '/home/claudio/physics/01_montepython/montepython-kauyumari/chains/N2_nakawe/bao_jla_planck/nkw_1-3_cluster1_f1.7/'])
roots = ['2018-12-10_800000_','2019-01-03_1000000_',]
params = [u'omega_b', u'omega_cdm', u'Omega_Lambda', u'b0_fld', u'b1_fld', u'b2_fld', u'H0']

param_3d = None
g.settings.alpha_filled_add=1

g.triangle_plot(roots, params, plot_3d_with_param=param_3d, filled=True, shaded=False
               ,legend_labels=[r'$w(N=2)$ BAO + JLA',r'$w(N=2)$ (PlanckTT + lowP) + BAO + JLA']
               ,legend_loc='upper right'
               ,line_args=[{'ls':'--', 'color':'darkblue'},{'lw':1, 'color':'orange'}]
               ,contour_colors=['darkblue','orange'])

g.export('prueba3_mp.pdf')
