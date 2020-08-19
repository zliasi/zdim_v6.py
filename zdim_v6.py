# ==============================================================================
# ==============================================================================
#
#   Modified dipole interaction model for computing the complex induced
#   dipole moment of Ag, Cu, Au, Al, Be, Cr, Ni, Pd, Pt, Ti, and W.
#
#   The polarizability is computed using either the Lorentz-Drude model (LD),
#   the extended Lorentz model (XL) or the Brendel-Bormann model (BB).
#
#   All values for the polarizability computations are from
#
#   Rakić et al. (1998):
#   https://doi.org/10.1364/AO.37.005271
#
#   Except for the static polarizabilites, which are from
#
#   Hillers-Bendtsen et al. (2019):
#    https://doi.org/10.1016/j.cplett.2019.136661
#
#   Schwerdtfeger et al. (2018):
#   https://doi.org/10.1080/00268976.2018.1535143
#
#   All code, including the zdimpy package, is written by Zacharias Liasi
#
#   GitHub repository: https://github.com/zliasi/zdim
#
#   Last edited: 19 Aug. 2020.
#
# ==============================================================================
# ==============================================================================

# ==============================================================================
#   MODULES
# ==============================================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from zdimpy import (
    fread as f,
    calc,
    plot
)

# ==============================================================================
#   SETTINGS
# ==============================================================================

element = "Ag"
model = "BB"

# Fields
E_external = np.array([5, 5, 5])
origin = np.array([0, 0, 0])

# Frequencies

freq_min = 0.1
freq_max = 15
npoints = 200
freq = np.logspace(
    np.log10(freq_min),
    np.log10(freq_max),
    npoints
)

# xyz file with coordinates
if element == "Ag":
    xyz_path = "/home/liasi/py/clusters/Ag_cluster.xyz"
if element == "Au":
    xyz_path = "/home/liasi/py/clusters/Au_cluster.xyz"
if element == "Cu":
    xyz_path = "/home/liasi/py/clusters/Cu_cluster.xyz"
if element == "Al":
    xyz_path = "/home/liasi/py/clusters/Al_cluster.xyz"
if element == "Be":
    xyz_path = "/home/liasi/py/clusters/Be_cluster.xyz"
if element == "Cr":
    xyz_path = "/home/liasi/py/clusters/Cr_cluster.xyz"
if element == "Ni":
    xyz_path = "/home/liasi/py/clusters/Ni_cluster.xyz"
if element == "Pd":
    xyz_path = "/home/liasi/py/clusters/Pd_cluster.xyz"
if element == "Pt":
    xyz_path = "/home/liasi/py/clusters/Pt_cluster.xyz"
if element == "Ti":
    xyz_path = "/home/liasi/py/clusters/Ti_cluster.xyz"
if element == "W":
    xyz_path = "/home/liasi/py/clusters/W_cluster.xyz"

# ==============================================================================
#   COORDINATES
# ==============================================================================

coordinates, x_coordinates, y_coordinates, z_coordinates = f.xyz(
    xyz_path
)

p_dist, o_dist = calc.spatial_dist(
    coordinates,
    origin
)

x_diff, y_diff, z_diff = calc.point_diff(
    coordinates
)

T_xx, T_yy, T_zz, T_xy, T_xz, T_yz = calc.T(
    x_diff,
    y_diff,
    z_diff,
    p_dist
)

temp_A = calc.tensor_stack(
    [
        T_xx,
        T_xy,
        T_xz,
        T_xy,
        T_yy,
        T_yz,
        T_xz,
        T_yz,
        T_zz
    ]
)

# ==============================================================================
#   COMPUTE POLARIZABILITES
# ==============================================================================

dip_x = []
dip_y = []
dip_z = []
abs_x = []
abs_y = []
abs_z = []

for i in freq:

    if model == "LD":
        alpha = calc.LD(element, i)
    elif model == "XL":
        alpha = calc.XL(element, i)
    elif model == "BB":
        alpha = calc.BB(element, i)

    # The array has to be complex, otherwise the imag part of alpha will be
    # discarded.
    temp_A = temp_A.astype(complex)
    np.fill_diagonal(temp_A, alpha)
    B = np.linalg.inv(temp_A)

    dipole_x = np.full((len(coordinates), 1), 1 + 0.j)
    dipole_y = np.full((len(coordinates), 1), 1 + 0.j)
    dipole_z = np.full((len(coordinates), 1), 1 + 0.j)

    counter = 0

    while True:

        counter += 1

        E = calc.E(o_dist, E_external, dipole_x, dipole_y, dipole_z,
                   coordinates, x_coordinates, y_coordinates, z_coordinates)

        dipole = np.dot(B, E)

        check_x = dipole[0:len(dipole):3]
        check_y = dipole[1:len(dipole):3]
        check_z = dipole[2:len(dipole):3]

        if (np.array_equal(dipole_x, check_x) == True
            and np.array_equal(dipole_y, check_y) == True
            and np.array_equal(dipole_z, check_z) == True
                or counter > 999):

            plot.dipole_append(
                dip_x,
                dip_y,
                dip_z,
                abs_x,
                abs_y,
                abs_z,
                dipole
            )

            break

        dipole_x = dipole[0:len(dipole):3]
        dipole_y = dipole[1:len(dipole):3]
        dipole_z = dipole[2:len(dipole):3]

dip_x = np.asarray(dip_x)
dip_y = np.asarray(dip_y)
dip_z = np.asarray(dip_z)
abs_x = np.asarray(abs_x)
abs_y = np.asarray(abs_y)
abs_z = np.asarray(abs_z)

# ==============================================================================
#   PLOTS
# ==============================================================================

plot.logplot(
    freq,
    dip_x,
    abs_x,
    model,
    element
)
