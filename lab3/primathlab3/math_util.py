import numpy
import scipy.sparse

def equals(a, b, eps):
    """
    сравнить numpy вектора с точностью eps
    """
    if (a is None) and (b is None):
        return True
    if (a is None) or (b is None):
        return False
    for i in range(a.size):
        if abs(a[i] - b[i]) > eps:
            return False
    return True

def empty_matrix(n, m):
    """Пустой нулевой двумерный массив
    :param n: количество строк
    :param m: количество столбцов
    :return: python array
    """
    return scipy.sparse.csr_matrix((n, m))


def identity_matrix(n):
    """Единичная матрица размера n в разреженном виде
    :param n: размерность матрицы nxn
    :return: матрица E
    """
    return scipy.sparse.identity(n, format="csr")


def ascending_vector(n):
    """Возвращает увеличивающийся вектор
    :param n: размерность
    :return: вектора вида (1, 2, ..., n)
    """
    x = numpy.empty(n)
    for i in range(n):
        x[i] = i + 1
    return x


def generate_big_matrix(n, p):
    """Генерирует большую матрицу nxn разреженности p
    :param n: размерность или порядок матрицы
    :param p: отношение ненулевых клеток к nxn
    :return: матрица A в разреженном виде
    """
    return scipy.sparse.random(n, n, p)


def random_vector(n):
    """Генерирует любой вектор размерности n
    для демонстрационных целей
    :param n: размерность
    :return: любой вектор x
    """
    return ascending_vector(n)

