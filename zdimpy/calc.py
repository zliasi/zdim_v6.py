import numpy as np
from scipy.special import wofz as w


def LD(element, freq):
    """
    Computes the polarizability of 1 of 11 metals using the Lorentz-Drude model.

    Parameters
    ----------
    freq : Array of frequency points (in eV) to be used for the calculations.

    element : String containing the name of the metal.

    Returns
    -------
    alpha : List of complex frequency dependent polarizabilites for the metal.

    Note
    ----
    All values are from

    Rakić et al. (1998):
    https://doi.org/10.1364/AO.37.005271
    """
    if element == "Ag":
        omega_p = 9.01  # eV
        f0 = 0.845
        gamma_0 = 0.048  # eV

        f1 = 0.065
        gamma_1 = 3.886  # eV
        omega_1 = 0.816  # eV

        f2 = 0.124
        gamma_2 = 0.452  # eV
        omega_2 = 4.481  # eV

        f3 = 0.011
        gamma_3 = 0.065  # eV
        omega_3 = 8.185  # eV

        f4 = 0.840
        gamma_4 = 0.916  # eV
        omega_4 = 9.083  # eV

        f5 = 5.646
        gamma_5 = 2.419  # eV
        omega_5 = 20.29  # eV

    elif element == "Au":
        omega_p = 9.03  # eV
        f0 = 0.760
        gamma_0 = 0.053  # eV

        f1 = 0.024
        gamma_1 = 0.241  # eV
        omega_1 = 0.415  # eV

        f2 = 0.010
        gamma_2 = 0.345  # eV
        omega_2 = 0.830  # eV

        f3 = 0.071
        gamma_3 = 0.870  # eV
        omega_3 = 2.969  # eV

        f4 = 0.601
        gamma_4 = 2.494  # eV
        omega_4 = 4.304  # eV

        f5 = 4.384
        gamma_5 = 2.214  # eV
        omega_5 = 13.32  # eV

    elif element == "Cu":
        omega_p = 10.83  # eV
        f0 = 0.575
        gamma_0 = 0.030  # eV

        f1 = 0.061
        gamma_1 = 0.378  # eV
        omega_1 = 0.291  # eV

        f2 = 0.104
        gamma_2 = 1.056  # eV
        omega_2 = 2.957  # eV

        f3 = 0.723
        gamma_3 = 3.213  # eV
        omega_3 = 5.300  # eV

        f4 = 0.638
        gamma_4 = 4.305  # eV
        omega_4 = 11.18  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Al":
        omega_p = 14.98  # eV
        f0 = 0.523
        gamma_0 = 0.047  # eV

        f1 = 0.227
        gamma_1 = 0.333  # eV
        omega_1 = 0.162  # eV

        f2 = 0.050
        gamma_2 = 0.312  # eV
        omega_2 = 1.544  # eV

        f3 = 0.166
        gamma_3 = 1.351  # eV
        omega_3 = 1.808  # eV

        f4 = 0.030
        gamma_4 = 3.382  # eV
        omega_4 = 3.473  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Be":
        omega_p = 18.51  # eV
        f0 = 0.084
        gamma_0 = 0.035  # eV

        f1 = 0.031
        gamma_1 = 1.664  # eV
        omega_1 = 0.100  # eV

        f2 = 0.140
        gamma_2 = 3.395  # eV
        omega_2 = 1.032  # eV

        f3 = 0.530
        gamma_3 = 4.454  # eV
        omega_3 = 3.183  # eV

        f4 = 0.130
        gamma_4 = 1.802  # eV
        omega_4 = 4.604  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Cr":
        omega_p = 10.75  # eV
        f0 = 0.168
        gamma_0 = 0.047  # eV

        f1 = 0.151
        gamma_1 = 3.175  # eV
        omega_1 = 0.121  # eV

        f2 = 0.150
        gamma_2 = 1.305  # eV
        omega_2 = 0.543  # eV

        f3 = 1.149
        gamma_3 = 2.676  # eV
        omega_3 = 1.970  # eV

        f4 = 0.825
        gamma_4 = 1.335  # eV
        omega_4 = 8.775  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Ni":
        omega_p = 15.92  # eV
        f0 = 0.096
        gamma_0 = 0.048  # eV

        f1 = 0.100
        gamma_1 = 4.511  # eV
        omega_1 = 0.174  # eV

        f2 = 0.135
        gamma_2 = 1.334  # eV
        omega_2 = 0.582  # eV

        f3 = 0.106
        gamma_3 = 2.178  # eV
        omega_3 = 1.597  # eV

        f4 = 0.729
        gamma_4 = 6.292  # eV
        omega_4 = 6.089  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Pd":
        omega_p = 9.72  # eV
        f0 = 0.330
        gamma_0 = 0.008  # eV

        f1 = 0.649
        gamma_1 = 2.950  # eV
        omega_1 = 0.336  # eV

        f2 = 0.121
        gamma_2 = 0.555  # eV
        omega_2 = 0.501  # eV

        f3 = 0.638
        gamma_3 = 4.621  # eV
        omega_3 = 1.659  # eV

        f4 = 0.453
        gamma_4 = 3.236  # eV
        omega_4 = 5.715  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Pt":
        omega_p = 9.59  # eV
        f0 = 0.333
        gamma_0 = 0.080  # eV

        f1 = 0.191
        gamma_1 = 0.517  # eV
        omega_1 = 0.780  # eV

        f2 = 0.659
        gamma_2 = 1.838  # eV
        omega_2 = 1.314  # eV

        f3 = 0.547
        gamma_3 = 3.668  # eV
        omega_3 = 3.141  # eV

        f4 = 3.576
        gamma_4 = 8.517  # eV
        omega_4 = 9.249  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "Ti":
        omega_p = 7.29  # eV
        f0 = 0.148
        gamma_0 = 0.082  # eV

        f1 = 0.899
        gamma_1 = 2.276  # eV
        omega_1 = 0.777  # eV

        f2 = 0.393
        gamma_2 = 2.518  # eV
        omega_2 = 1.545  # eV

        f3 = 0.187
        gamma_3 = 1.663  # eV
        omega_3 = 2.509  # eV

        f4 = 0.001
        gamma_4 = 1.762  # eV
        omega_4 = 19.43  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    elif element == "W":
        omega_p = 13.22  # eV
        f0 = 0.206
        gamma_0 = 0.064  # eV

        f1 = 0.054
        gamma_1 = 0.530  # eV
        omega_1 = 1.004  # eV

        f2 = 0.166
        gamma_2 = 1.281  # eV
        omega_2 = 1.917  # eV

        f3 = 0.706
        gamma_3 = 3.332  # eV
        omega_3 = 3.580  # eV

        f4 = 2.590
        gamma_4 = 5.836  # eV
        omega_4 = 7.498  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

    Omega_p = f0**0.5 * omega_p  # eV

    def LD_comp(freq):
        dielec = 1-Omega_p**2/(freq*(freq+1j*gamma_0))
        dielec += f1*omega_p**2 / ((omega_1**2-freq**2)-1j*freq*gamma_1)
        dielec += f2*omega_p**2 / ((omega_2**2-freq**2)-1j*freq*gamma_2)
        dielec += f3*omega_p**2 / ((omega_3**2-freq**2)-1j*freq*gamma_3)
        dielec += f4*omega_p**2 / ((omega_4**2-freq**2)-1j*freq*gamma_4)
        dielec += f5*omega_p**2 / ((omega_5**2-freq**2)-1j*freq*gamma_5)
        return dielec

    dielec = LD_comp(freq)

    V = 18403
    alpha = V * ((dielec-1) / (1+(1/3)*(dielec-1)))

    return (
        alpha
    )


def XL(element, freq):
    """
    Computes the polarizability of 1 of 11 metals using the extended Lorentz
    model.

    Parameters
    ----------
    freq : Array of frequency points (in eV) to be used for the calculations.

    element : String containing the name of the metal.

    Returns
    -------
    alpha : List of complex frequency dependent polarizabilites for the metal.

    Note
    ----
    All values are from

    Rakić et al. (1998):
    https://doi.org/10.1364/AO.37.005271

    Except for the static polarizabilites, which are from

    Hillers-Bendtsen et al. (2019):
    https://doi.org/10.1016/j.cplett.2019.136661

    Schwerdtfeger et al. (2018):
    https://doi.org/10.1080/00268976.2018.1535143
    """
    if element == "Ag":
        omega_p = 9.01  # eV

        f1 = 0.065
        gamma_1 = 3.886  # eV
        omega_1 = 0.816  # eV

        f2 = 0.124
        gamma_2 = 0.452  # eV
        omega_2 = 4.481  # eV

        f3 = 0.011
        gamma_3 = 0.065  # eV
        omega_3 = 8.185  # eV

        f4 = 0.840
        gamma_4 = 0.916  # eV
        omega_4 = 9.083  # eV

        f5 = 5.646
        gamma_5 = 2.419  # eV
        omega_5 = 20.29  # eV

        stat_pol = 49.9843*27.211324570273  # eV

    elif element == "Au":
        omega_p = 9.03  # eV
        f0 = 0.760
        gamma_0 = 0.053  # eV

        f1 = 0.024
        gamma_1 = 0.241  # eV
        omega_1 = 0.415  # eV

        f2 = 0.010
        gamma_2 = 0.345  # eV
        omega_2 = 0.830  # eV

        f3 = 0.071
        gamma_3 = 0.870  # eV
        omega_3 = 2.969  # eV

        f4 = 0.601
        gamma_4 = 2.494  # eV
        omega_4 = 4.304  # eV

        f5 = 4.384
        gamma_5 = 2.214  # eV
        omega_5 = 13.32  # eV

        stat_pol = 31.0400*27.211324570273  # eV

    elif element == "Cu":
        omega_p = 10.83  # eV
        f0 = 0.575
        gamma_0 = 0.030  # eV

        f1 = 0.061
        gamma_1 = 0.378  # eV
        omega_1 = 0.291  # eV

        f2 = 0.104
        gamma_2 = 1.056  # eV
        omega_2 = 2.957  # eV

        f3 = 0.723
        gamma_3 = 3.213  # eV
        omega_3 = 5.300  # eV

        f4 = 0.638
        gamma_4 = 4.305  # eV
        omega_4 = 11.18  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 33.7420*27.211324570273  # eV

    elif element == "Al":
        omega_p = 14.98  # eV
        f0 = 0.523
        gamma_0 = 0.047  # eV

        f1 = 0.227
        gamma_1 = 0.333  # eV
        omega_1 = 0.162  # eV

        f2 = 0.050
        gamma_2 = 0.312  # eV
        omega_2 = 1.544  # eV

        f3 = 0.166
        gamma_3 = 1.351  # eV
        omega_3 = 1.808  # eV

        f4 = 0.030
        gamma_4 = 3.382  # eV
        omega_4 = 3.473  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 57.8*27.211324570273  # eV

    elif element == "Be":
        omega_p = 18.51  # eV
        f0 = 0.084
        gamma_0 = 0.035  # eV

        f1 = 0.031
        gamma_1 = 1.664  # eV
        omega_1 = 0.100  # eV

        f2 = 0.140
        gamma_2 = 3.395  # eV
        omega_2 = 1.032  # eV

        f3 = 0.530
        gamma_3 = 4.454  # eV
        omega_3 = 3.183  # eV

        f4 = 0.130
        gamma_4 = 1.802  # eV
        omega_4 = 4.604  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 37.74*27.211324570273  # eV

    elif element == "Cr":
        omega_p = 10.75  # eV
        f0 = 0.168
        gamma_0 = 0.047  # eV

        f1 = 0.151
        gamma_1 = 3.175  # eV
        omega_1 = 0.121  # eV

        f2 = 0.150
        gamma_2 = 1.305  # eV
        omega_2 = 0.543  # eV

        f3 = 1.149
        gamma_3 = 2.676  # eV
        omega_3 = 1.970  # eV

        f4 = 0.825
        gamma_4 = 1.335  # eV
        omega_4 = 8.775  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 83*27.211324570273  # eV

    elif element == "Ni":
        omega_p = 15.92  # eV
        f0 = 0.096
        gamma_0 = 0.048  # eV

        f1 = 0.100
        gamma_1 = 4.511  # eV
        omega_1 = 0.174  # eV

        f2 = 0.135
        gamma_2 = 1.334  # eV
        omega_2 = 0.582  # eV

        f3 = 0.106
        gamma_3 = 2.178  # eV
        omega_3 = 1.597  # eV

        f4 = 0.729
        gamma_4 = 6.292  # eV
        omega_4 = 6.089  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 49*27.211324570273  # eV

    elif element == "Pd":
        omega_p = 9.72  # eV
        f0 = 0.330
        gamma_0 = 0.008  # eV

        f1 = 0.649
        gamma_1 = 2.950  # eV
        omega_1 = 0.336  # eV

        f2 = 0.121
        gamma_2 = 0.555  # eV
        omega_2 = 0.501  # eV

        f3 = 0.638
        gamma_3 = 4.621  # eV
        omega_3 = 1.659  # eV

        f4 = 0.453
        gamma_4 = 3.236  # eV
        omega_4 = 5.715  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 26.14*27.211324570273  # eV

    elif element == "Pt":
        omega_p = 9.59  # eV
        f0 = 0.333
        gamma_0 = 0.080  # eV

        f1 = 0.191
        gamma_1 = 0.517  # eV
        omega_1 = 0.780  # eV

        f2 = 0.659
        gamma_2 = 1.838  # eV
        omega_2 = 1.314  # eV

        f3 = 0.547
        gamma_3 = 3.668  # eV
        omega_3 = 3.141  # eV

        f4 = 3.576
        gamma_4 = 8.517  # eV
        omega_4 = 9.249  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 48*27.211324570273  # eV

    elif element == "Ti":
        omega_p = 7.29  # eV
        f0 = 0.148
        gamma_0 = 0.082  # eV

        f1 = 0.899
        gamma_1 = 2.276  # eV
        omega_1 = 0.777  # eV

        f2 = 0.393
        gamma_2 = 2.518  # eV
        omega_2 = 1.545  # eV

        f3 = 0.187
        gamma_3 = 1.663  # eV
        omega_3 = 2.509  # eV

        f4 = 0.001
        gamma_4 = 1.762  # eV
        omega_4 = 19.43  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 100*27.211324570273  # eV

    elif element == "W":
        omega_p = 13.22  # eV
        f0 = 0.206
        gamma_0 = 0.064  # eV

        f1 = 0.054
        gamma_1 = 0.530  # eV
        omega_1 = 1.004  # eV

        f2 = 0.166
        gamma_2 = 1.281  # eV
        omega_2 = 1.917  # eV

        f3 = 0.706
        gamma_3 = 3.332  # eV
        omega_3 = 3.580  # eV

        f4 = 2.590
        gamma_4 = 5.836  # eV
        omega_4 = 7.498  # eV

        f5 = 0
        gamma_5 = 0  # eV
        omega_5 = 0  # eV

        stat_pol = 68*27.211324570273  # eV

    def XL_comp(freq):
        dielec = f1*omega_p**2 / ((omega_1**2-freq**2)-1j*freq*gamma_1)
        dielec += f2*omega_p**2 / ((omega_2**2-freq**2)-1j*freq*gamma_2)
        dielec += f3*omega_p**2 / ((omega_3**2-freq**2)-1j*freq*gamma_3)
        dielec += f4*omega_p**2 / ((omega_4**2-freq**2)-1j*freq*gamma_4)
        dielec += f5*omega_p**2 / ((omega_5**2-freq**2)-1j*freq*gamma_5)
        alpha = stat_pol * dielec
        return alpha

    alpha = XL_comp(freq)

    return (
        alpha
    )


def BB(element, freq):
    """
    Computes the polarizability of 1 of 11 metals using the Brendel-Bormann
    model.

    Parameters
    ----------
    freq : Array of frequency points (in eV) to be used for the calculations.

    element : String containing the name of the metal.

    Returns
    -------
    alpha : List of complex frequency dependent polarizabilites for the metal.

    Note
    ----
    All values are from

    Rakić et al. (1998):
    https://doi.org/10.1364/AO.37.005271
    """
    if element == "Ag":
        omega_p = 9.01  # eV
        f0 = 0.821
        gamma_0 = 0.049  # eV

        f1 = 0.050
        gamma_1 = 0.189  # eV
        omega_1 = 2.025  # eV
        sigma_1 = 1.894  # eV

        f2 = 0.133
        gamma_2 = 0.067  # eV
        omega_2 = 5.185  # eV
        sigma_2 = 0.665  # eV

        f3 = 0.051
        gamma_3 = 0.019  # eV
        omega_3 = 4.343  # eV
        sigma_3 = 0.189  # eV

        f4 = 0.467
        gamma_4 = 0.117  # eV
        omega_4 = 9.809  # eV
        sigma_4 = 1.170  # eV

        f5 = 4.000
        gamma_5 = 0.052  # eV
        omega_5 = 18.56  # eV
        sigma_5 = 0.516  # eV

    elif element == "Au":
        omega_p = 9.03  # eV
        f0 = 0.770
        gamma_0 = 0.050  # eV

        f1 = 0.054
        gamma_1 = 0.074  # eV
        omega_1 = 0.218  # eV
        sigma_1 = 0.742  # eV

        f2 = 0.050
        gamma_2 = 0.035  # eV
        omega_2 = 2.885  # eV
        sigma_2 = 0.349  # eV

        f3 = 0.312
        gamma_3 = 0.083  # eV
        omega_3 = 4.069  # eV
        sigma_3 = 0.830  # eV

        f4 = 0.719
        gamma_4 = 0.125  # eV
        omega_4 = 6.137  # eV
        sigma_4 = 1.246  # eV

        f5 = 1.648
        gamma_5 = 0.179  # eV
        omega_5 = 27.97  # eV
        sigma_5 = 1.795  # eV

    elif element == "Cu":
        omega_p = 10.83  # eV
        f0 = 0.562
        gamma_0 = 0.030  # eV

        f1 = 0.076
        gamma_1 = 0.056  # eV
        omega_1 = 0.416  # eV
        sigma_1 = 0.562  # eV

        f2 = 0.081
        gamma_2 = 0.047  # eV
        omega_2 = 2.849  # eV
        sigma_2 = 0.469  # eV

        f3 = 0.324
        gamma_3 = 0.113  # eV
        omega_3 = 4.819  # eV
        sigma_3 = 1.131  # eV

        f4 = 0.726
        gamma_4 = 0.172  # eV
        omega_4 = 8.136  # eV
        sigma_4 = 1.719  # eV

    elif element == "Al":
        omega_p = 14.98  # eV
        f0 = 0.526
        gamma_0 = 0.047  # eV

        f1 = 0.213
        gamma_1 = 0.312  # eV
        omega_1 = 0.163  # eV
        sigma_1 = 0.013  # eV

        f2 = 0.060
        gamma_2 = 0.315  # eV
        omega_2 = 1.561  # eV
        sigma_2 = 0.042  # eV

        f3 = 0.182
        gamma_3 = 1.587  # eV
        omega_3 = 1.827  # eV
        sigma_3 = 0.256  # eV

        f4 = 0.014
        gamma_4 = 2.145  # eV
        omega_4 = 4.495  # eV
        sigma_4 = 1.735  # eV

    elif element == "Be":
        omega_p = 18.51  # eV
        f0 = 0.081
        gamma_0 = 0.035  # eV

        f1 = 0.066
        gamma_1 = 2.956  # eV
        omega_1 = 0.131  # eV
        sigma_1 = 0.277  # eV

        f2 = 0.067
        gamma_2 = 3.962  # eV
        omega_2 = 0.469  # eV
        sigma_2 = 3.167  # eV

        f3 = 0.346
        gamma_3 = 2.398  # eV
        omega_3 = 2.827  # eV
        sigma_3 = 1.446  # eV

        f4 = 0.311
        gamma_4 = 3.904  # eV
        omega_4 = 4.318  # eV
        sigma_4 = 0.893  # eV

    elif element == "Cr":
        omega_p = 10.75  # eV
        f0 = 0.154
        gamma_0 = 0.048  # eV

        f1 = 0.338
        gamma_1 = 4.256  # eV
        omega_1 = 0.281  # eV
        sigma_1 = 0.115  # eV

        f2 = 0.261
        gamma_2 = 3.957  # eV
        omega_2 = 0.584  # eV
        sigma_2 = 0.252  # eV

        f3 = 0.817
        gamma_3 = 2.218  # eV
        omega_3 = 1.919  # eV
        sigma_3 = 0.225  # eV

        f4 = 0.105
        gamma_4 = 6.983  # eV
        omega_4 = 6.997  # eV
        sigma_4 = 4.903  # eV

    elif element == "Ni":
        omega_p = 15.92  # eV
        f0 = 0.083
        gamma_0 = 0.022  # eV

        f1 = 0.357
        gamma_1 = 2.820  # eV
        omega_1 = 0.317  # eV
        sigma_1 = 0.606  # eV

        f2 = 0.039
        gamma_2 = 0.120  # eV
        omega_2 = 1.059  # eV
        sigma_2 = 1.454  # eV

        f3 = 0.127
        gamma_3 = 1.822  # eV
        omega_3 = 4.583  # eV
        sigma_3 = 0.379  # eV

        f4 = 0.654
        gamma_4 = 6.637  # eV
        omega_4 = 8.825  # eV
        sigma_4 = 0.510  # eV

    elif element == "Pd":
        omega_p = 9.72  # eV
        f0 = 0.330
        gamma_0 = 0.009  # eV

        f1 = 0.769
        gamma_1 = 2.343  # eV
        omega_1 = 0.066  # eV
        sigma_1 = 0.694  # eV

        f2 = 0.093
        gamma_2 = 0.497  # eV
        omega_2 = 0.502  # eV
        sigma_2 = 0.027  # eV

        f3 = 0.309
        gamma_3 = 2.022  # eV
        omega_3 = 2.432  # eV
        sigma_3 = 1.167  # eV

        f4 = 0.409
        gamma_4 = 0.119  # eV
        omega_4 = 5.987  # eV
        sigma_4 = 1.331  # eV

    elif element == "Pt":
        omega_p = 9.59  # eV
        f0 = 0.333
        gamma_0 = 0.080  # eV

        f1 = 0.186
        gamma_1 = 0.498  # eV
        omega_1 = 0.782  # eV
        sigma_1 = 0.031  # eV

        f2 = 0.665
        gamma_2 = 1.851  # eV
        omega_2 = 1.317  # eV
        sigma_2 = 0.096  # eV

        f3 = 0.551
        gamma_3 = 2.604  # eV
        omega_3 = 3.189  # eV
        sigma_3 = 0.766  # eV

        f4 = 2.214
        gamma_4 = 2.891  # eV
        omega_4 = 8.236  # eV
        sigma_4 = 1.146  # eV

    elif element == "Ti":
        omega_p = 7.29  # eV
        f0 = 0.126
        gamma_0 = 0.067  # eV

        f1 = 0.427
        gamma_1 = 1.877  # eV
        omega_1 = 1.459  # eV
        sigma_1 = 0.463  # eV

        f2 = 0.218
        gamma_2 = 0.100  # eV
        omega_2 = 2.661  # eV
        sigma_2 = 0.506  # eV

        f3 = 0.513
        gamma_3 = 0.615  # eV
        omega_3 = 0.805  # eV
        sigma_3 = 0.799  # eV

        f4 = 0.0002
        gamma_4 = 4.109  # eV
        omega_4 = 19.86  # eV
        sigma_4 = 2.854  # eV

    elif element == "W":
        omega_p = 13.22  # eV
        f0 = 0.197
        gamma_0 = 0.057  # eV

        f1 = 0.006
        gamma_1 = 3.689  # eV
        omega_1 = 0.481  # eV
        sigma_1 = 3.754  # eV

        f2 = 0.022
        gamma_2 = 0.277  # eV
        omega_2 = 0.985  # eV
        sigma_2 = 0.059  # eV

        f3 = 0.136
        gamma_3 = 1.433  # eV
        omega_3 = 1.962  # eV
        sigma_3 = 0.273  # eV

        f4 = 2.648
        gamma_4 = 4.555  # eV
        omega_4 = 5.442  # eV
        sigma_4 = 1.912  # eV

    Omega_p = f0**.5 * omega_p  # eV

    if element == "Ag" or "Au":
        def BB_comp(freq):
            dielec = 1-Omega_p**2/(freq*(freq+1j*gamma_0))

            alpha = (freq**2+1j*freq*gamma_1)**0.5
            za = (alpha-omega_1)/(2**.5*sigma_1)
            zb = (alpha+omega_1)/(2**.5*sigma_1)
            dielec += 1j*np.pi**.5*f1*omega_p**2 / \
                (2**1.5*alpha*sigma_1) * (w(za)+w(zb))  # χ1

            alpha = (freq**2+1j*freq*gamma_2)**0.5
            za = (alpha-omega_2)/(2**.5*sigma_2)
            zb = (alpha+omega_2)/(2**.5*sigma_2)
            dielec += 1j*np.pi**.5*f2*omega_p**2 / \
                (2**1.5*alpha*sigma_2) * (w(za)+w(zb))  # χ2

            alpha = (freq**2+1j*freq*gamma_3)**0.5
            za = (alpha-omega_3)/(2**.5*sigma_3)
            zb = (alpha+omega_3)/(2**.5*sigma_3)
            dielec += 1j*np.pi**.5*f3*omega_p**2 / \
                (2**1.5*alpha*sigma_3) * (w(za)+w(zb))  # χ3

            alpha = (freq**2+1j*freq*gamma_4)**0.5
            za = (alpha-omega_4)/(2**.5*sigma_4)
            zb = (alpha+omega_4)/(2**.5*sigma_4)
            dielec += 1j*np.pi**.5*f4*omega_p**2 / \
                (2**1.5*alpha*sigma_4) * (w(za)+w(zb))  # χ4

            alpha = (freq**2+1j*freq*gamma_5)**0.5
            za = (alpha-omega_5)/(2**.5*sigma_5)
            zb = (alpha+omega_5)/(2**.5*sigma_5)
            dielec += 1j*np.pi**.5*f5*omega_p**2 / \
                (2**1.5*alpha*sigma_5) * (w(za)+w(zb))  # χ5

            return dielec

    # if element == "Cu" or "Ti" or "Al" or "Be" or "Cr" or "Ni" or "Pd" or "Pt" or "Ti" or "W":
    if element == set(["Cu", "Al", "Be", "Cr", "Ni", "Pd", "Pt", "Ti", "W"]):
        def BB_comp(freq):
            dielec = 1-Omega_p**2/(freq*(freq+1j*gamma_0))

            alpha = (freq**2+1j*freq*gamma_1)**0.5
            za = (alpha-omega_1)/(2**.5*sigma_1)
            zb = (alpha+omega_1)/(2**.5*sigma_1)
            dielec += 1j*np.pi**.5*f1*omega_p**2 / \
                (2**1.5*alpha*sigma_1) * (w(za)+w(zb))  # χ1

            alpha = (freq**2+1j*freq*gamma_2)**0.5
            za = (alpha-omega_2)/(2**.5*sigma_2)
            zb = (alpha+omega_2)/(2**.5*sigma_2)
            dielec += 1j*np.pi**.5*f2*omega_p**2 / \
                (2**1.5*alpha*sigma_2) * (w(za)+w(zb))  # χ2

            alpha = (freq**2+1j*freq*gamma_3)**0.5
            za = (alpha-omega_3)/(2**.5*sigma_3)
            zb = (alpha+omega_3)/(2**.5*sigma_3)
            dielec += 1j*np.pi**.5*f3*omega_p**2 / \
                (2**1.5*alpha*sigma_3) * (w(za)+w(zb))  # χ3

            alpha = (freq**2+1j*freq*gamma_4)**0.5
            za = (alpha-omega_4)/(2**.5*sigma_4)
            zb = (alpha+omega_4)/(2**.5*sigma_4)
            dielec += 1j*np.pi**.5*f4*omega_p**2 / \
                (2**1.5*alpha*sigma_4) * (w(za)+w(zb))  # χ4

            return dielec

    dielec = BB_comp(freq)

    V = 18403
    alpha = V * ((dielec-1) / (1+(1/3)*(dielec-1)))

    return (
        alpha
    )


def spatial_dist(coordinates, origin):
    """
    Computes the spatial distance between each atom as well as the spatial
    distance from the origin (centre of cluster) to each atom.

    Parameters
    ----------
    coordinates : Array containing the coordinates of the atoms.

    Returns
    -------
    p_dist : Spatial distance between each atom.

    o_dist : Spatial distance from the origin to each atom.
    """
    return (
        np.linalg.norm(coordinates - coordinates[:, None], axis=-1),
        np.linalg.norm(origin - coordinates[:, None], axis=-1)
    )


def point_diff(coordinates):
    """
    Computes the difference between each x-coordinate, each y-coordinate, and
    each z-coordinate, respectively, i.e. (x_n - x_m), (y_n - y_m), and
    (z_n - z_m).

    Parameters
    ----------
    coordinates : Array containing the coordinates for the atoms.

    Returns
    -------
    x_diff : Difference between each of the x-coordinates.

    y_diff : Difference between each of the y-coordinates.

    z_diff : Difference between each of the z-coordinates.
    """
    return (
        (coordinates - coordinates[:, None])[..., 0],
        (coordinates - coordinates[:, None])[..., 1],
        (coordinates - coordinates[:, None])[..., 2]
    )


def T(x_diff, y_diff, z_diff, p_dist):
    """
    Computes the real second-order dipole interaction tensors.

    Parameters
    ----------
    x_diff : Difference between all the x-coordinates.

    y_diff : Difference between all the y-coordinates.

    z_diff : Difference between all the z-coordinates.

    p_dist : Spatial distance between each atom.

    Returns
    -------
    T_xx : Array containing all the xx components.

    T_yy : Array containing all the yy components.

    T_zz : Array containing all the zz components.

    T_xy : Array containing all the xy components.

    T_xz : Array containing all the xz components.

    T_yz : Array containing all the yz components.
    """
    with np.errstate(divide="ignore", invalid="ignore"):
        T_xx = ((3 * x_diff**2) / p_dist**5) - (1 / p_dist**3)
        T_yy = ((3 * y_diff**2) / p_dist**5) - (1 / p_dist**3)
        T_zz = ((3 * z_diff**2) / p_dist**5) - (1 / p_dist**3)
        T_xy = ((3 * x_diff * y_diff) / p_dist**5)
        T_xz = ((3 * x_diff * z_diff) / p_dist**5)
        T_yz = ((3 * z_diff * y_diff) / p_dist**5)

    T_xx[np.isnan(T_xx)] = 0
    T_yy[np.isnan(T_yy)] = 0
    T_zz[np.isnan(T_zz)] = 0
    T_xy[np.isnan(T_xy)] = 0
    T_xz[np.isnan(T_xz)] = 0
    T_yz[np.isnan(T_yz)] = 0

    return (
        T_xx,
        T_yy,
        T_zz,
        T_xy,
        T_xz,
        T_yz
    )


def tensor_stack(arrays):
    """
    Reshapes a touple of arrays in accordance with the shape of the A matrix.

    Parameters
    ----------
    arrays : Touple of arrays.

    Returns
    -------
    array : Total array with the proper shape.
    """
    arrays = np.asarray(arrays)
    n, p, q = arrays.shape
    s = int(round(np.sqrt(n)))
    arrays = arrays.reshape(s, -1, p, q)

    return arrays.transpose(2, 0, 3, 1).reshape(s * p, -1)


def E(
    o_dist,
    E_external,
    dipole_x,
    dipole_y,
    dipole_z,
    coordinates,
    x_coordinates,
    y_coordinates,
    z_coordinates
):
    """
    Computes the Cartesian components of the permanent electrical field, and
    combines them into an array stored under the variable name E.

    Parameters
    ----------
    E_external : Array containing the Cartesian components of the external
                 electrical field.

    dipole_x : Array containing the x components of the induced dipole
               moments for both the molecule and nanoparticle.

    dipole_y : Array containing the y components of the induced dipole
               moments for both the molecule and nanoparticle.

    dipole_z : Array containing the z components of the induced dipole
               moments for both the molecule and nanoparticle.

    o_dist : Spatial distance from the origin (centre of the cluster) to each
             atom.

    x_coordinates : Array containing the x-coordinates from the given .xyz file.

    y_coordinates : Array containing the y-coordinates from the given .xyz file.

    z_coordinates : Array containing the z-coordinates from the given .xyz file.

    Returns
    -------
    E : Array containing the values of the permanent electrical field.
    """
    E_x = E_external[0] + ((-1) * (
        dipole_x * (1 / (o_dist**3) - 3 * ((x_coordinates**2) / (o_dist**5)))
        + dipole_y * ((- 3 * x_coordinates * y_coordinates) / o_dist**5)
        + dipole_z * (-(3 * x_coordinates * z_coordinates) / o_dist**5)
    ))

    E_y = E_external[1] + ((-1) * (
        dipole_y * (1 / (o_dist**3) - 3 * ((y_coordinates**2) / (o_dist**5)))
        + dipole_x * ((- 3 * y_coordinates * x_coordinates) / o_dist**5)
        + dipole_z * (- (3 * y_coordinates * z_coordinates) / o_dist**5)
    ))

    E_z = E_external[2] + ((-1) * (
        dipole_z * (1 / (o_dist**3) - 3 * ((z_coordinates**2) / (o_dist**5)))
        + dipole_y * ((- 3 * z_coordinates * y_coordinates) / o_dist**5)
        + dipole_x * (-(3 * y_coordinates * z_coordinates) / o_dist**5)
    ))

    E = []
    for element in zip(E_x, E_y, E_z):
        E.extend(element)

    E = np.asarray(E)
    E = E.astype(complex)

    return E
