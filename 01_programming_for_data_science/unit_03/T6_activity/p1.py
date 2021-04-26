import numpy as np


def q1():
    series = [[23,45,12,679], [14,48,69,38]]
    new_series = np.array(series)
    print(new_series.ndim)
    print(new_series.shape)



def q2():
    a = np.zeros(10) + 4
    print(a)
    print("--------------")

    a = np.zeros(10) * 4
    print(a)
    print("--------------")

    a = np.ones(10) * 4
    print(a)
    print("--------------")

    a = np.ones(10) + 4
    print(a)
    print("--------------")

    a = np.full(10, 4)
    print(a)
    print("--------------")


def q3():
    dataset = np.array(['paul', 'jacob', 'vince', 'paul', 'miky', 'larence', 'warren'])
    print(dataset == 'paul')


def q4():
    percentiles = [98, 76.37, 55.55, 69, 88]
    first_subject = np.array(percentiles)
    print(first_subject.dtype.name)



def q5():


    print("--------------")
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[::2] = -1
    print(arr)

    print("--------------")
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[1::2] = -1
    print(arr)

    print("--------------")
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[arr % 2 == 0] = -1
    print(arr)

    print("--------------")
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    arr[-2::-2] = -1
    print(arr)


def q6():
    print("--------------")
    arr = np.eye(5)
    arr[arr == 0] = -1
    print(arr)

    print("--------------")
    arr = np.eye(5)
    arr[arr != 1] = -1
    print(arr)

    print("--------------")
    arr = np.eye(5)
    # arr = np.full((5x5),-1)
    print(arr)

    print("--------------")
    arr = np.eye(5)
    arr = arr - (np.eye(5) + 1)
    print(arr)




def main():
    q6()


main()