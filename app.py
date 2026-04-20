from flask import Flask, jsonify
import requests
import json
from urllib.parse import quote
import os

app = Flask(__name__)

ED_USERNAME = os.environ.get("ED_USERNAME")
ED_PASSWORD = os.environ.get("ED_PASSWORD")

@app.route('/test_login')
def test_login():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    session.get("https://api.ecoledirecte.com/v3/login.awp?gtk=1&v=4.75.0", headers=headers)
    login_data = {"identifiant": ED_USERNAME, "motdepasse": ED_PASSWORD, "isRelogin": False, "uuid": ""}
    payload = "data=" + quote(json.dumps(login_data))
    resp = session.post("https://api.ecoledirecte.com/v3/login.awp?v=4.75.0", headers=headers, data=payload)
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
