import streamlit as st
import pandas as pd
import streamlit_option_menu
from streamlit_option_menu import option_menu
import openai
from langchain.prompts import ChatPromptTemplate
import google.generativeai as genai

st.set_page_config(
    page_title="",
    page_icon=" ",
    layout="wide"
)



col1, col2 = st.columns([28, 5])
with col2:
    st.image("ash.jpg",width=200)
with col1:
    st.markdown('<p style="color: #000066; font-size:50px;font-family: Garamond;">Jessica and Grace AI Hub(Beta)</p>', unsafe_allow_html=True)





# Option menu
with st.sidebar:
   st.markdown('<p style="color: #000066; font-size:30px;font-family: Arial;">AI Tools</p>', unsafe_allow_html=True) 
    
   selected = option_menu(
        menu_title="",  # Required to make it work
        options=["Academic Practice","Other"],
        icons=["book", "book"],
        menu_icon="cast",
        default_index=0,
    )
    

# Main content
if selected == "Academic Practice":
    st.markdown('<p style="color: #000066; font-size:50px;font-family: Garamond;">Weclcome to Academic Practice</p>', unsafe_allow_html=True)
    
    genai.configure(api_key="AIzaSyAr2P7KqFTdyqavDAMRdDjzYzTFlUYI90c")
    
    st.markdown('<p style="color:#000066; font-size:30px;font-family: Garamond;">Enter the course name:</p>', unsafe_allow_html=True)
    course_name = st.text_input("",key="course_name_input")
    
    st.markdown('<p style="color:#000066; font-size:30px;font-family: Garamond;">Select your Grade:</p>', unsafe_allow_html=True)
    grade = st.selectbox(
        "",
        ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    )
    


    template_string1 = """Please give me one {subject} problem, I am a grade {grader} student."""
    
    def generate_math_problem():
        prompt = template_string1.format(subject=course_name, grader=grade)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
              
        return response.text
    
    def check_answer(problem, user_answer):
        prompt = f"problem: {problem}\nUser's answer: {user_answer}\nIs the answer correct?"
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        
        return response.text
    
       
    
   
    if 'math_problem' not in st.session_state:
        st.session_state.math_problem = generate_math_problem()
    if 'user_answer' not in st.session_state:
        st.session_state.user_answer = ''
    if 'result' not in st.session_state:
        st.session_state.result = ''
    
    if st.button("Next Question"):
      st.session_state.math_problem = generate_math_problem()
      st.session_state.user_answer = ''
      st.session_state.result = ''
      st.experimental_rerun() 
      
    st.markdown('<p style="color:#000066; font-size:30px;font-family: Garamond;">Problems:</p>', unsafe_allow_html=True)
    st.session_state.math_problem = st.text_area("", st.session_state.math_problem, height=300)
    

    st.markdown('<p style="color:#000066; font-size:30px;font-family: Garamond;">Please Input Your Answer:</p>', unsafe_allow_html=True)
    user_answer = st.text_input("", st.session_state.user_answer)
    

    if user_answer:
        st.session_state.user_answer = user_answer
        st.session_state.result = check_answer(st.session_state.math_problem, st.session_state.user_answer)
    
    st.markdown('<p style="color:#000066; font-size:30px;font-family: Garamond;">Result:</p>', unsafe_allow_html=True)
    st.write(st.session_state.result)
    


        
