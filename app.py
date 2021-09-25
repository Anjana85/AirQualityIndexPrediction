import numpy as np
from flask import Flask,render_template,url_for,request,jsonify
import pandas as pd 

import pickle

# load the model from disk
model=pickle.load(open('random_forest_regression_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        T= float(request.form['T'])
        TM= float(request.form['TM'])
        Tm= float(request.form['Tm'])
        SLP= float(request.form['SLP'])
        H= int(request.form['H'])
        VV= float(request.form['VV'])
        V= float(request.form['V'])
        VM= float(request.form['VM'])
        prediction=model.predict([[T,TM,Tm,SLP,H,VV,V,VM]])
        output=round(prediction[0],2)
        
        return render_template('home.html', prediction_text='AirQualityindex is $ {}'.format(output))
    else:
       return render_template('home.html')



if __name__ == '__main__':
	app.run(debug=True)