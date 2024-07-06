import json
import random


# generates a random square matrix of size n
def gen_sq_matrix(n):
    return [[random.random() for i in range(n)] for _ in range(n)]


def dump_matrix(matrix, filename):
    with open(filename, 'w') as f:
        json.dump(matrix, f)


def add_matrices(matrix1, matrix2):
    added_matrix = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        added_matrix.append(row)
    return added_matrix


def multiply_matrices(matrix1, matrix2):
    multiplied_matrix = [[0 for i in range(len(matrix2[0]))]
                         for j in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return multiplied_matrix
