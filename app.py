from tensorflow.keras.models import load_model
import streamlit as st
import time
model=load_model('car_price_model1')

@st.cache()


def prediction(drivewheel,enginelocation,carlength,carwidth,curbweight,enginesize,fuelsystem,horsepower,citympg,highwaympg):
  if drivewheel=='fwd':
    drivewheel=1
  elif drivewheel=='rwd':
    drivewheel=2
  else:
    drivewheel=0
    

  if enginelocation=='front':
    enginelocation=0
  else:
    enginelocation=1
    
    

  

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
    
 
  
  
  values=[[drivewheel,enginelocation,carlength,carwidth,curbweight,enginesize,fuelsystem,horsepower,citympg,highwaympg]]
  prediction=model.predict(values)
  prediction=prediction[0][0]
  return prediction

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;padding:13px"> 
    <h1 style ="color:white;text-align:center;">Car Price Prediction developed by M.Waqar Gul</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    drivewheel= st.selectbox('Drive-wheel',("fwd","rwd","4wd"))
    enginelocation = st.selectbox('Engine-location',("front","rear")) 
    carlength =st.number_input('Car-length')
    carwidth =st.number_input('Car-width')       
    curbweight =st.number_input('Curb-weight')                                           
    enginesize=st.number_input('Engine-size')
    fuelsystem=st.selectbox('Fuel-system',("mpfi","2bbl","idi","1bbl","spdi","4bbl","mfi","spfi"))
    horsepower = st.number_input("Horse Power") 
    citympg = st.number_input("City-mpg") 
    highwaympg = st.number_input("Highway-mpg")
    result =""
                                            
    if st.button("Predict"): 
        result = prediction(drivewheel,enginelocation,carlength,carwidth,curbweight,enginesize,fuelsystem,horsepower,citympg,highwaympg) 
        progress_bar = st.progress(0)
        progress_text = st.empty()
        for i in range(101):
            time.sleep(0.1)
            progress_bar.progress(i)
            progress_text.text(f"Progress: {i}%")
        st.success('Car price is ${}'.format(round(result,2)))
        print(result)
                                            

if __name__=='__main__':
                                            main()
  
  
  
   
    
