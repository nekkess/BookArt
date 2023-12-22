import requests

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/api/book"
    json = {'text': 'Dostoyevsky The Devils'}
    r = requests.get(url, json)
    print(r.content)