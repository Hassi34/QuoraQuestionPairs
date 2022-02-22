# Importing essential libraries
from flask import Flask, render_template, request
import pickle, gzip, helper
import numpy as np
from flask_cors import cross_origin

with gzip.open("model.pickle.gz" , "rb") as f:
    classifier = pickle.load(f)
app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('index.html')

@app.route('/predict_duplicates', methods=['POST'])
@cross_origin()
def predict_duplicates():
    if request.method == 'POST':
        if request.json is not None:
            question1 = request.json['question1']
            question2 = request.json['question2']
            query = helper.query_point_creator(question1,question2)
            prediction = classifier.predict(query)[0]
            probability_not_duplicate = (classifier.predict_proba(query)[0][0])*100
            if prediction == 0 :
                return f'Questions are NOT Duplicated || Duplicated Probability = {100-probability_not_duplicate}% || Not Duplicated Probability = {probability_not_duplicate}%'
            elif prediction == 1:
                return f'Questions are Duplicated || Duplicated Probability = {100-probability_not_duplicate}% || Not Duplicated Probability = {probability_not_duplicate}%'
            else:
                return "This is not valid input for prediction!"
        elif request.form is not None:
            question1 = request.form['question1']
            question2 = request.form['question2']
            
            query = helper.query_point_creator(question1,question2)
            prediction = classifier.predict(query)[0]
            probability_not_duplicate = (classifier.predict_proba(query)[0][0])*100      
            return render_template('result.html', prediction=prediction, probability_not_duplicate = probability_not_duplicate)

if __name__ == '__main__':
	app.run(debug=False)