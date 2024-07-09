import csv
import json
from collections import deque
from matrix_ops import multiply_matrices, gen_sq_matrix, add_matrices
from pyinstrument import Profiler
from pyinstrument.renderers import JSONRenderer

# to run this code and generate the pyinstrument_profile.csv file
trace_id = 1

with Profiler() as p:
    matrix1 = gen_sq_matrix(500)
    matrix2 = gen_sq_matrix(500)
    matrix3 = add_matrices(matrix1, matrix2)
    matrix4 = multiply_matrices(matrix1, matrix3)

obj = json.loads(p.output(JSONRenderer()))
with open('pyinstrument_profile.json', 'w') as f:
    json.dump(obj, f, indent=4)

with open('pyinstrument_profile.csv', 'w') as f:
    writer = csv.DictWriter(
        f, fieldnames=['trace_id', 'function', 'time', 'stack'])
    writer.writeheader()

    queue = deque([obj['root_frame']])
    while queue:
        frame = queue.popleft()

        parent_stack = frame['parent_stack'] if 'parent_stack' in frame else ''
        stack = parent_stack + '->' + frame['file_path_short'] + ':' + frame[
            'function'] if parent_stack else frame[
                'file_path_short'] + ':' + frame['function']

        writer.writerow({
            'trace_id': trace_id,
            'function': frame['function'],
            'stack': stack,
            'time': frame['time']
        })
        if 'children' in frame:
            for child in frame['children']:
                queue.append({
                    'function': child['function'],
                    'file_path_short': child['file_path_short'],
                    'parent_stack': stack,
                    'time': child['time'],
                    'children': child['children']
                })
