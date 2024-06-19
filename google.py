

import google.generativeai as genai

genai.configure(api_key="AIzaSyAr2P7KqFTdyqavDAMRdDjzYzTFlUYI90c")





template_string1 = """Please give me one {subject} problem, I am a grade {grader} student."""

def generate_math_problem():
    prompt = template_string1.format(subject="math", grader=8)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
          
    return response.text

x=generate_math_problem()

print(x)