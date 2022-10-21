def task1(x, y):
    S = x**2 + y**2
    return S

def task2(s):
    k = 0
    for i in s:
        if i.isalpha() == False and i.isdigit() == False:
            k += 1
    return k
             
def task3(s):
        S = s.split()
    k = 0
    for x in s:
        if x[0] == 'a' and x[1] == 'b' and x[len(x)-2] == 'b' and x[len(x)-1] == 'a':
            k += 1
    return k
    
def task4(generator):
    def filt(x):
        k = 0
        for i in len(x) - 2:
            if x[i] == 'u' and x[i+1] == 's' and x[i+2] == 'u':
                k += 1
        if k == 0:
            return True
        else:
            return False
    lis = filter(filt, generator)
    return lis

def task5(list_of_smth):
    for i in range (len(list_of_smth) - 2, 1, -3):
        return list_of_smth[i]

def task6(list1, list2, list3, list4):
    list12 = set(list1+list2)
    list34 = set(list3+list4)
    list = set(list12) & set(list34)
    return list
         
def task7():
    import numpy as np
    from numpy import linalg as la
    matrix = np.random.randint(0, 25, (5, 5))
    matrix1 = np.delete(matrix, 0, axis = 0)
    matrix1 = np.delete(matrix1, 3, axis = 1)
    return matrix, matrix1

def task8(f, min_x, max_x, N, min_y, max_y):
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.plot(x, y, 'b-')
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.xscale('log')
    plt.grid('True')
    x = np.linspace(min_x, max_x)
    dx = max_x - min_x
    dydx = np.gradient(y, dx)
    plt.show()
    plt.savefig("function.pdf")

def task9(data, x_array, y_array, threshold):

def task10(list_of_smth, n):
    n = len(list_of_smth)
    for i in range(n):
        SUM = 0
        for j in range(i+1, n):
            SUM += list_of_smth[j]**2
            list_of_smth[i] = (SUM/(n-i))**0.5
    return list_of_smth

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    # TODO: ...
