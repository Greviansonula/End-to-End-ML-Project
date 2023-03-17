from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.perprocessing import StandardScaler


application=Flask(__name__)

app = application

## Route for home pad
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/prediction', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        pass