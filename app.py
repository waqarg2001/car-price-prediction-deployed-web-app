from flask import Flask, render_template,request
from tensorflow.keras.models import load_model
import requests

model=load_model('car_price_model1')

app=Flask(__name__)
@app.route('/')
def home():
  return render_template('Home.html')

@app.route('/predict',methods=['POST'])
def predict():
  drivewheel=request.form['drive_wheel']
  if drivewheel=='fwd':
    drivewheel=1
  elif drivewheel=='rwd':
    drivewheel=2
  else:
    drivewheel=0
    
  enginelocation=request.form['engine_location']
  if enginelocation=='front':
    enginelocation=0
  else:
    enginelocation=1
    
    
  carlength=int(request.form['car_length'])
  carwidth=int(request.form['car_width'])
  curbweight=int(request.form['curb_weight'])
  enginesize=int(request.form['engine_size'])
  
  fuelsystem=request.form['fuel_system']
  if fuelsystem=='mpfi':
    fuelsystem=5
  elif fuelsystem=='2bbl':
    fuelsystem=1
  elif fuelsystem=='idi':
    fuelsystem=3
  elif fuelsystem=='1bbl':
    fuelsystem=0
  elif fuelsystem=='spdi':
    fuelsystem=6
  elif fuelsystem=='4bbl':
    fuelsystem=2
  elif fuelsystem=='mfi':
    fuelsystem=7
  else:
    fuelsystem=4
    
  horsepower=int(request.form['horse_power'])
  citympg=int(request.form['city_mpg'])
  highwaympg=int(request.form['highway_mpg'])
  
  
  values=[[drivewheel,enginelocation,carlength,carwidth,curbweight,enginesize,fuelsystem,horsepower,citympg,highwaympg]]
  prediction=model.predict(values)
  prediction=round(pred[0],2)
  return render_template('Home.html',pred=f"Car price is ${prediction}")


if __name__=='__main__':
  app.run(debug=True)
  
  
  
   
    
