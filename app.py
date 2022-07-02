from flask import Flask, render_template, request
import pickle
import category_encoders as ce
import model as m
import pandas as pd
# from requests import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/lifestyle_analyser")
def lifestyle_analyser():
    return render_template('la.html')

@app.route("/lifestyle_analyser1")
def lifestyle_analyser1():
    return render_template('la1.html')

# @app.route("/recommendation")
# def recommendation():
#     return render_template('recommendation.html')

@app.route("/recommendations1")
def recommendations1():
    return render_template('recommendations1.html')
model = pickle.load(open('model.pkl','rb'))

@app.route('/recommendation', methods = ['GET','POST'])
def recommendation():
    if request.method == "POST":
      name2 = request.form.to_dict()
      name = pd.DataFrame.from_dict([name2])
      print(name)
      pred = m.disease_pred(name)
      print(pred[0][1])
      global diabetes,bloodp, hd, ad, td, sd, bs, ha , pcd, can
      if pred[0][0] == 1:
          diabetes = "You might suffer from Diabetes"
      else:
          diabetes = "Diabetes not detected"

      if pred[0][1] == 1:
          bloodp = "You might suffer from bp"
      else:
          bloodp = "BP not detected"

      if pred[0][2] == 1:
          hd = "You might suffer from heart related disease"
      else:
          hd = "Heart related disease not detected"

      if pred[0][3] == 1:
          ad = "You might suffer from Alzheimer's Disease"
      else:
          ad = "Alzheimer's Disease not detected"

      if pred[0][4] == 1:
           td = "You might suffer from Thyroid"
      else:
           td = "Thyroid not detected"

      if pred[0][5] == 1:
           sd = "You might suffer from Skin related diseases"
      else:
           sd = " Skin related diseases not detected"

      if pred[0][6] == 1:
           bs = "You might suffer from Brain Stroke"
      else:
           bs = "Brain Stroke not detected"  

      if pred[0][7] == 1:
           ha = "You might suffer from Hairfall"
      else:
           ha = "Low Hairfall detected"

      if pred[0][8] == 1:
           pcd = "You might suffer from PCOS/PCOD"
      else:
           pcd = "PCOS/PCOD not detected"

      if pred[0][9] == 1:
           can = "You might suffer from Cancer"  
      else:
           can = "Cancer not detected"  
    return render_template('recommendation.html', a= diabetes , b= bloodp, c = hd, d= ad, e= td, f= sd, g=bs, h= ha,i=pcd,j=can) 


if __name__ == "__main__":
    app.run(debug=True)