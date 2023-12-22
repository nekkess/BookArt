from flask import Flask, request, render_template, jsonify
import requests
import random
import os
from openai import OpenAI, AsyncOpenAI
from database import Database
from config import Config
from flask_cors import CORS


os.environ["API_KEY"] = Config.API_KEY

# openai.api_key = os.getenv("API_KEY")
client = AsyncOpenAI(
  api_key=os.getenv("API_KEY"),  # this is also the default, it can be omitted
)


app = Flask(__name__)
# CORS(app)

db = Database(os.path.join("assets", "artists.csv"))


@app.route('/api/book', methods=['GET'])
async def index():
    user_prompt = request.args.get('text')

    print(request.args)

    if not user_prompt:
        return "No answer."

    print('Sending request')

    completion = await client.chat.completions.create(
        model="gpt-4", 
        # model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": Config.SYSTEM_RULE_PAINTING},
            {"role": "user", "content": user_prompt}]
        )

    print('Recieved response')
    gpt_response = completion.choices[0].message.content
    print(gpt_response)
    found = db.get_url(gpt_response)
    name = found['name'].values[0].replace(' ','_')
    print(name)

    chuj = random.choice(os.listdir(os.path.join("assets", "images", "images", name)))
    print(chuj)

    # return jsonify({'author_name': str(gpt_response.strip())})
    return jsonify({"file_path": str(chuj)})


if __name__ == '__main__':
    app.run(debug=True)
    