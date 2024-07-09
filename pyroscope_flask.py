import time
from flask import Flask, request, g, make_response
import os
import pyroscope

from matrix_ops import multiply_matrices, gen_sq_matrix, add_matrices

# to run this code, first launch a pyroscope server:
# docker run -d --name pyroscope -p 4040:4040 grafana/pyroscope

# then run the python server
# pip install pyroscope-io
# FLASK_APP=pyroscope_flask.py python3 -m flask run

# then to run and profile this code, open:
# http://localhost:5000/

# then open the pyroscope UI to see the profile:
# http://localhost:4040/

pyroscope.configure(
    application_name="khq.profiledemo.app",
    server_address="http://localhost:4040",
    sample_rate=100,  # default is 100
    detect_subprocesses=False,
    oncpu=True,  # report cpu time only; default is True
    gil_only=True,
    enable_logging=True,
    tags={
        "region": f'{os.getenv("REGION")}',
    })

app = Flask(__name__)


@app.route("/")
def home():
    matrix1 = gen_sq_matrix(1000)
    matrix2 = gen_sq_matrix(1000)
    matrix3 = add_matrices(matrix1, matrix2)
    matrix4 = multiply_matrices(matrix1, matrix3)
    return ' '.join([
        ' '.join([str(matrix4[i][j]) for j in range(500)]) for i in range(500)
    ])
