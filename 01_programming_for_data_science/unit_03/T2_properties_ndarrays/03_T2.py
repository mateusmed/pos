import numpy as np


def format_quantity_dim():
    a1d = np.random.randint(0, 10, 10)
    print(a1d)
    print(a1d.shape) # verifica o formato do array
    print(a1d.ndim) # quantidade de dimensões

    a2d = np.random.randint(1, 101, (4, 5))
    print(a2d)
    print(a2d.shape)
    print(a2d.ndim)

    a3d = np.random.random((3, 4, 5))
    print(a3d)
    print(a3d.shape)
    print(a3d.ndim)


def main():
    format_quantity_dim()


main()