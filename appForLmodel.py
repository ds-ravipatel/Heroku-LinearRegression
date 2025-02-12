import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('LR_Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #using below - parameters will be stored in list
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = np.round(prediction[0],2)
    return render_template('index.html', prediction_text='Salary should be $ {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)