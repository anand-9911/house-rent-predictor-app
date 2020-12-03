import streamlit as st
import pickle
import pandas as pd
import numpy as np

pickle_in=open("deploy2.pkl","rb")
rent=pickle.load(pickle_in)

def predict_rent(rooms,bathroom,parking_spaces,floor,city_Chennai,city_Delhi,city_Kolkata,city_Mumbai,pet,furnished):
    prediction=rent.predict([[rooms,bathroom,parking_spaces,floor,city_Chennai,city_Delhi,city_Kolkata,city_Mumbai,pet,furnished]])
    print(prediction)
    return np.round(prediction,2)

def main():
    """ NNN """
    html_temp="""
    <div style="background-color:#20786b;padding:15px">
    <h1 style="color:yellow;text-align:center">Metro City House Rent Estimator</h1>
    
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    #city=st.radio("Select city",("Delhi","Bangalore","Mumbai","Kolkata","Chennai"))
    city=st.selectbox("Select city",["Delhi","Bangalore","Mumbai","Kolkata","Chennai"])
    if city=='Delhi':
        city_Delhi=0
        city_Chennai=1
        city_Mumbai=1
        city_Kolkata=1
        city_Bangalore=1
    elif city=='Mumbai':
        city_Mumbai=0
        city_Delhi=1
        city_Chennai=1
        city_Kolkata=1
        city_Bangalore=1
    elif city=='Chennai':
        city_Chennai=0
        city_Delhi=1
        city_Mumbai=1
        city_Kolkata=1
        city_Bangalore=1
    elif city=='Kolkata':
        city_Kolkata=0
        city_Delhi=1
        city_Mumbai=1
        city_Chennai=1
        city_Bangalore=1
    else:
        city_Bangalore=0
        city_Delhi=1
        city_Chennai=1
        city_Mumbai=1
        city_Kolkata=1

    room=st.slider("Select number of rooms",15,1)

    bathroom=st.slider("Select number of bathrooms",10,1)

    parking_spaces=st.slider("Select number of parking spaces",15,0)

    flr=st.slider("Select floor preference",30,0)

    pet=st.radio("Do you have pets?",("Yes","No"))
    if pet=="Yes":
        pet=1
    else:
        pet=0

    furnished=st.radio("Do you want furnished house?",("Yes","No"))
    if furnished=="Yes":
        furnished=0
    else:
        furnished=1



    if st.button("ESTIMATE RENT"):
        #result=predict_rent(room,bathroom,parking_spaces,flr)
        st.success("Estimated rent is Rs. {}".format(predict_rent(room,bathroom,parking_spaces,flr,city_Chennai,city_Delhi,city_Kolkata,city_Mumbai,pet,furnished)[0]))

if __name__=='__main__':
    main()
