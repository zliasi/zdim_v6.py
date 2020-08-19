import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def dipole_append(
    dip_x,
    dip_y,
    dip_z,
    abs_x,
    abs_y,
    abs_z,
    dipole
):
    """
    Appends the complex induced dipole moment values to the given lists.

    Parameters
    ----------
    dip_x : Array containing the real x-values of the computed moment.

    dip_y : Array containing the real y-values of the computed moment.

    dip_z : Array containing the real z-values of the computed moment.

    abs_x : Array containing the imag x-values of the computed moment.

    abs_y : Array containing the imag y-values of the computed moment.

    abs_z : Array containing the imag z-values of the computed moment.

    dipole : Array containing of the computed moment.

    """
    return (
        dip_x.append(np.real(np.sum(dipole[0:len(dipole):3]))),
        dip_y.append(np.real(np.sum(dipole[1:len(dipole):3]))),
        dip_z.append(np.real(np.sum(dipole[2:len(dipole):3]))),
        abs_x.append(np.imag(np.sum(dipole[0:len(dipole):3]))),
        abs_y.append(np.imag(np.sum(dipole[1:len(dipole):3]))),
        abs_z.append(np.imag(np.sum(dipole[2:len(dipole):3])))
    )


def logplot(.
    freq,
    dip_x,
    abs_x,
    model,
    element
):
    plt.rc('font', **{'family': 'serif', 'serif': ['Palatino']}, size='8')
    plt.rc('text', usetex=True)

    plt.rc('xtick', labelsize=7)
    plt.rc('ytick', labelsize=7)

    fig, (ax1) = plt.subplots(1, 1, sharex=True,
                              sharey=True, figsize=(3.409449, 2.130906), dpi=600)

    ax2 = ax1.twiny()
    ax2.plot(freq, abs(dip_x), label=r"${Re}(\mu)$", color='none')
    ax1.plot(freq, abs(dip_x), label=r"${Re}(\mu)$",
             color='k', linewidth=1, linestyle='--')
    ax1.plot(freq, abs(abs_x), label=r"${Im}(\mu)$",
             color='k', linewidth=1)

    legend = ax1.legend(loc=3, borderaxespad=0.25, fontsize=7)
    frame = legend.get_frame()
    frame.set_facecolor('1.0')
    frame.set_edgecolor('1.0')

    ax1.set_xlabel('Photon energy (eV)')
    ax1.xaxis.labelpad = 3
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlim([0.1, 7])
    ax1.set_xticks([0.1, 1, 5, 7, 10, 15])
    ax1.set_xticklabels((0.1, 1, 5, 7, 10, 15))

    ax2.set_xscale('log')
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks([0.1239841874, 1.239841874, 4.959367496, 12.3984])
    ax2.set_xticklabels((r'$10^4$', r'$10^3$', 250, 100))
    ax2.set_xlabel(r"Wavelength (nm)")
    ax2.xaxis.labelpad = 5

    string1 = ("{} / {}".format(model, element))
    ax1.text(0.01, 0.94, string1, color='k', transform=ax1.transAxes, fontsize=6.5,
             bbox=dict(boxstyle="square",
                       ec="white",
                       fc="white",
                       alpha=0.90
                       )
             )

    plt.savefig(
        "zdim_v6_{0}_{1}".format(model, element),
        bbox_inches='tight'
    )

    plt.close("all")
