from flask import Flask, render_template, request
import jsonify
import requests
import joblib
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = joblib.load('filename.pkl')
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        RandD = int(request.form['RandD'])
        Administration =float(request.form['Administration'])
        Marketting_spent = float(request.form['Marketting_spent'])
        # Kms_Driven2=np.log(Kms_Driven)
        State_Florida = request.form['State_Florida']
        if(State_Florida == 'Florida'):
            State_Florida = 1
            State_New_York=0
        else:
            State_Florida = 0
            State_New_York = 1
        
        prediction = model.predict(
            [[RandD, Administration, Marketting_spent, State_Florida, State_New_York]])
        output = round(prediction[0], 2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)