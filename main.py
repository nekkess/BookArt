from flask import Flask, request, render_template
import requests
import os
import openai   
from config import Config

os.environ["API_KEY"] = Config.API_KEY

openai.api_key = os.getenv("API_KEY")


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    user_prompt = request.args.get('text')
    if not user_prompt:
        return "No answer."
        
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": Config.SYSTEM_RULE},
            {"role": "user", "content": user_prompt}
            ]
            )
    return completion.choices[0].message


if __name__ == '__main__':
    app.run(debug=True)
