import os
import numpy as np
from montepython.likelihood_class import Likelihood_prior

class distance_prior(Likelihood_prior):

	# initialisation of the class is done within the parent Likelihood_prior. For
	# this case, it does not differ, actually, from the __init__ method in
	# Likelihood class.

	def loglkl(self, cosmo, data):
	
		omegab, omegac, theta = (
			data.mcmc_parameters[p]['current']*data.mcmc_parameters[p]['scale']
			for p in ['omega_b', 'omega_cdm', '100*theta_s'])
		diffvec = np.array([x-mu for x, mu in zip([omegab, omegac, theta], self.centre)])
		loglkl = -0.5 * np.dot(diffvec.T, np.dot(self.invcov, diffvec))
		return loglkl
