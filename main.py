from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # input = requests.get("http://127.0.0.1:5000/", {"text":"Nigga"}).text
    user = request.args.get('text')
    if user:
        return user
    return "no text"


if __name__ == '__main__':
    app.run(debug=True)
