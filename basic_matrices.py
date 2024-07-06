import time
import cProfile
from matrix_ops import gen_sq_matrix, dump_matrix, add_matrices, multiply_matrices


def main():
    matrix1 = gen_sq_matrix(500)
    matrix2 = gen_sq_matrix(500)
    dump_matrix(matrix1, './matrix_data_1.json')
    dump_matrix(matrix2, './matrix_data_2.json')
    matrix3 = add_matrices(matrix1, matrix2)
    dump_matrix(matrix3, './matrix_data_3.json')
    matrix4 = multiply_matrices(matrix1, matrix2)
    dump_matrix(matrix4, './matrix_data_4.json')


enable_cProfile = True

if __name__ == '__main__':
    start_time = time.time()
    if enable_cProfile is True:
        pr = cProfile.Profile()
        pr.enable()
    main()
    if enable_cProfile is True:
        pr.disable()
    end_time = time.time()
    if enable_cProfile is True:
        pr.dump_stats('./cprofile.out')
    print(f'Time taken: {end_time - start_time}')
