import streamlit as st
import pandas as pd
st.title('Demo Project')
col1 , col2 = st.columns(2)
with col1:
    st.image('D:\Documents\Desktop\git-demo\download (1).jpeg')

with col2:
    st.write("""Good morning sir/ma’am. My name is Hunny Agarwal. I am a computer science student with a strong interest in software development and problem-solving. I have knowledge of programming in C++, along with concepts of OOP, DBMS, SQL, and data structures. I have also worked on projects involving database management and application development, which helped me improve my practical and technical skills. I am a quick learner, hardworking, and always interested in learning new technologies. My goal is to start my career in a reputed organization where I can apply my skills, gain practical experience, and continuously grow as a software professional. Thank you.""")

st.header('MY SKILLS')
st.subheader('Data Structures and Algorithms / Problem solving')
st.subheader('Data Analyst')
st.subheader('Machine Learning')
st.subheader('Web Development')
st.subheader('Database Management')
st.subheader('SQL')
st.subheader('C++')
st.subheader('Python')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About 
- Help
- Contact Us
""")