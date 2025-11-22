from flask import Flask, request, render_template
import os 
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    if request.method == 'POST':
        # Ensure that the form data is converted to appropriate data types
        try:
            var1 = float(request.form["dt"])
            var2 = float(request.form["AverageTemperature"])
            var3 = float(request.form["City"])
            var4 = float(request.form["Country"])
            var5 = float(request.form["Latitude"])
            var6 = float(request.form["Longitude"])
            

            # Convert the input data into a numpy array
            predict_data = np.array([var1, var2, var3, var4, var5, var6]).reshape(1, -1)

            # Use the loaded model to make predictions
            predict = model.predict(predict_data)
            print(predict)
            

        except ValueError:
            # Handle the case where form data cannot be converted to numeric types
            return render_template('output.html', predict="Error: Invalid input data")

    return render_template("output.html",predict = 'Predicted Average Temperture Uncertainity is' + ' ' +str(predict))

if __name__ == "__main__":
    app.run(debug=False, port=1111)