import requests
import streamlit as st
import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, send_from_directory

load_dotenv()

openai.api_key = os.getenv("API_KEY")

app = Flask(__name__)

option = st.selectbox(
    'Choose the type of the inspirational quote you wish to read:',
    ('Religious', 'Historic', 'Scientific', 'Computer Sciences', 'Other'))

@app.route("/")
def quote():
  prompt = "Fetch me an inspirational quote related to ",option
  
  print("Prompt is: ", prompt)
  
  return gpt(prompt)


def gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )

    return response.choices[0].message.content

@app.route('/.well-known/ai-plugin.json')
def serve_ai_plugin():
  return send_from_directory('./well-known',
                             'ai-plugin.json',
                             mimetype='application/json')


@app.route('/openapi.yaml')
def serve_openapi_yaml():
  return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')

# if __name__ == "__main__":
#   app.run(host='0.0.0.0', port=81)