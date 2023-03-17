from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictionPipeline


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
        data = CustomData(
            gender = request.get('gender'), 
            race_ethnicity = request.get("ethnicity"), 
            parental_level_of_education = request.get("parental_level_of_education"), 
            lunch = request.get("lunch"), 
            test_preparation_course = request.get("test_preparation_course"), 
            reading_score = request.get("writing_score"), 
            writing_score = request.get("reading_score")
            )

        pred_df = data.get_data_as_data_frame()
        print(print_df)

        predict_pipeline = PredictionPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)