# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:37:35 2024

@author: chenc
"""

from langchain.prompts import ChatPromptTemplate

template_string1 = """please give me one {subject} problems, I am {grader} student."""

template_string2 = """the {subject} problems is {}, a {grader} student provide the answer is {answer}.\
    Based on the problem and the answer, please tell the student whether the answer is right. If it is wrong,\
        tell the right answer, and why?"""
    

prompt_template1 = ChatPromptTemplate.from_template(template_string1)
prompt_template2 = ChatPromptTemplate.from_template(template_string2)

customer_messages = prompt_template1.format_messages(
                    subject=customer_style,
                    text=customer_email)