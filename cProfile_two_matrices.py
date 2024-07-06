import time
import cProfile
from matrix_ops import gen_sq_matrix, dump_matrix, add_matrices, multiply_matrices


def main():
    matrix1_small = gen_sq_matrix(100)
    matrix2_small = gen_sq_matrix(100)

    matrix3_large = gen_sq_matrix(500)
    matrix4_large = gen_sq_matrix(500)
    matrix5 = multiply_matrices(matrix1_small, matrix2_small)
    matrix6 = multiply_matrices(matrix3_large, matrix4_large)


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
        pr.dump_stats('./two_matrices.out')
    print(f'Time taken: {end_time - start_time}')
