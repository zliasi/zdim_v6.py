import numpy as np


def xyz(path):
    """
    Reads the given .xyz file and stores the values in an array.

    Parameters
    ----------
    path : The absolute file path of the .xyz file.

    Returns
    -------
    coordinates : Array containing the coordinates from the .xyz file.
    """
    coordinates = []
    x_coordinates = []
    y_coordinates = []
    z_coordinates = []

    with open(path) as fp:
        n_atoms = fp.readline()
        title = fp.readline()
        for line in fp:
            atom, x, y, z = line.split()
            coordinates.append([float(x), float(y), float(z)])
            x_coordinates.append([float(x)])
            y_coordinates.append([float(y)])
            z_coordinates.append([float(z)])

    return (
        np.asarray(coordinates),
        np.asarray(x_coordinates),
        np.asarray(y_coordinates),
        np.asarray(z_coordinates)
    )
