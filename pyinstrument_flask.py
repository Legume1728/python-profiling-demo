import time
from flask import Flask, request, g, make_response
from pyinstrument import Profiler
from matrix_ops import multiply_matrices, gen_sq_matrix, add_matrices

# to run this code
# FLASK_APP=pyinstrument_flask.py python3 -m flask run

# then to run and profile this code, open:
# http://localhost:5000/?profile

app = Flask(__name__)


@app.before_request
def before_request():
    if "profile" in request.args:
        g.profiler = Profiler()
        g.profiler.start()


@app.after_request
def after_request(response):
    if not hasattr(g, "profiler"):
        return response
    g.profiler.stop()
    output_html = g.profiler.output_html()
    return make_response(output_html)


@app.route("/")
def home():
    matrix1 = gen_sq_matrix(500)
    matrix2 = gen_sq_matrix(500)
    matrix3 = add_matrices(matrix1, matrix2)
    matrix4 = multiply_matrices(matrix1, matrix3)
    return ' '.join([
        ' '.join([str(matrix4[i][j]) for j in range(500)]) for i in range(500)
    ])
