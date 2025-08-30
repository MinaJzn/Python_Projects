import streamlit as st
from Password_Generatore import random_passwords,memorable_password,pin_codes

st.image('D:\Python\My_Exercise_Or_My_Project\Generate Password\Dashboard of project\images\streamlit-dashboard.png',width=550)
st.title(' :lock: Password Generatore:')


option=st.radio(
    'Select a Password Generator:',
    ('Random Password','Pin Codes','Memorable Password')
)

if option=='Pin Codes':
    length=st.slider('Select the length of Pin Code:',4,20,8)
    st.write(f'Your Password is  ```{pin_codes(length)}``` ')   
elif option=="Memorable Password":
    length=st.slider('Select the length of Pin Code:',6,10)
    st.write(f'Your Password is  ```{memorable_password(length)}``` ')
elif option=='Random Password':
    length=st.slider('Select the length of Pin Code:',8,50)
    st.write(f'Your Password is  ```{random_passwords(length)}``` ')


