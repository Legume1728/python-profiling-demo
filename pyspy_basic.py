import time
from matrix_ops import gen_sq_matrix, dump_matrix, add_matrices, multiply_matrices

# to run py-spy with this script, run the following command:
# py-spy record -o profile.svg -- python pyspy_basic.py

# to run py-spy on a running process, run the following command:
# py-spy record -o profile2.svg top -p <pid>

# to get a top view of the script, run the following command:
# py-spy top -- python pyspy_basic.py

# to get a callgraph, run the following command:
# py-spy record -f raw -o profile.collapse -- python pyspy_basic.py
# apt install graphviz
# gprof2dot -f collapse profile.collapse | dot -Tpng -o profile.png
# for more on graphviz and dot: https://graphviz.org/docs/layouts/dot/


def main():
    matrix1 = gen_sq_matrix(500)
    matrix2 = gen_sq_matrix(500)
    dump_matrix(matrix1, './matrix_data_1.json')
    dump_matrix(matrix2, './matrix_data_2.json')
    matrix3 = add_matrices(matrix1, matrix2)
    dump_matrix(matrix3, './matrix_data_3.json')
    matrix4 = multiply_matrices(matrix1, matrix2)
    dump_matrix(matrix4, './matrix_data_4.json')


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print(f'Time taken: {end_time - start_time}')
