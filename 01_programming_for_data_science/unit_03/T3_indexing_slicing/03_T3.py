import numpy as np


def create_array_1d():
    print('[create_array_1d]')
    print('----------')
    a1d = np.random.randint(0, 10, 10)
    print(a1d)
    print('----------')
    return a1d

def create_array_2d():
    print('[create_array_2d]')
    print('----------')
    a2d = np.random.randint(1, 101, (4, 5))
    print(a2d)
    print('----------')
    return a2d


def create_array_3d():
    print('[create_array_3d]')
    print('----------')
    a3d = np.random.random((3, 4, 5))
    print(a3d)
    print('----------')
    return a3d


def retrivie_data_example():
    print('[retrivie_data_example]')
    print('----------')
    a1d = create_array_1d()
    print(a1d[0])
    print(a1d[2])
    print(a1d[-1])
    print('----------')


def list_indices_access():
    print('list_indices_access')
    print('----------')
    indices = [3, 0, -1]
    a1d = create_array_1d()
    response = a1d[indices]
    print("response ", response)
    print('----------')



def get_index_2d():
    print('[get_index_2d]')
    print('----------')
    a2d = create_array_2d()
    print('first element: ', a2d[0][0])
    print('----------')


def get_content_by_index_2d():
    print('[get_content_by_index_list]')
    print('----------')
    a2d = create_array_2d()

    index_lin = [0, 1, 2, 3]
    index_col = [0, 1, 2, 3]

    print('elements: ', a2d[index_lin, index_col])

    index_lin = [0, 1, 2, 3]
    index_col = [3, 2, 1, 0]

    print('elements: ', a2d[index_lin, index_col])


    index_col = [3, 2, 1, 0]

    print('elements: ', a2d[ : , index_col])
    print('----------')



def get_content_by_index_3d():
    print('----------')
    print('[get_content_by_index_3d]')
    a3d = create_array_3d()

    print('pagina 2 linha 0 coluna 3:')
    print('valor: ', a3d[2][0][3])
    print('----------')


def main():
    create_array_1d()
    create_array_2d()
    create_array_3d()
    retrivie_data_example()
    list_indices_access()
    get_index_2d()
    get_content_by_index_2d()
    get_content_by_index_3d()

main()