import streamlit as st 
import Monty_Hall
import time

st.title(':door: Monty Hall Simulation')

st.image('D:\Python\My_Exercise_Or_My_Project\Monty Hall\Dashboard of monty hall\image\Monty Hall.png', width=400)

number_of_game=st.number_input('Enter number of games to simulate:',min_value=1,max_value=100000,value=100)

col1,col2=st.columns(2)
col1.subheader('Win Percentage without Switching')
col2.subheader('Win Percentage with Switching')

chart1=col1.line_chart(x=None,y=None)
chart2=col2.line_chart(x=None,y=None)


wins_no_switch = 0
wins_switch = 0
for i in range(1,number_of_game+1):
    num_wins_without_switching=(Monty_Hall.monty_hall(1, False))
    num_wins_with_switching =(Monty_Hall.monty_hall(1,True ))
    
    wins_no_switch += num_wins_without_switching
    wins_switch += num_wins_with_switching
    
    chart1.add_rows([wins_no_switch / (i + 1)])
    chart2.add_rows([wins_switch / (i + 1)])
    
    time.sleep(0.01)
    