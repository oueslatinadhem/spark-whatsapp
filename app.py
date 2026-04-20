from flask import Flask, jsonify
import requests
import json
from urllib.parse import quote
import os

app = Flask(__name__)

ED_USERNAME = os.environ.get("ED_USERNAME")
ED_PASSWORD = os.environ.get("ED_PASSWORD")

FA = [
    {"cn": "ED_UExVTUVfMDc1MjkxMUdfMV8xMDg0Mg==", "cv": "NzM0NDUwMzU0YTMyNGY2Yzc3NGIzMDcyMzI0ZTY2NjU0MTYxNDQ0ZjVhNTk3NzRjNDQ0NTMwNDY1MzQx", "uniq": False},
    {"cn": "ED_UExVTUVfMDc1MjkxMUdfRV85NTU5", "cv": "NTk2ZDc3NGU0MzZmNDQ0NzRhNGUzMjU2MzE3OTM3Njk3ODJiNDM3MjU0MzE1MzY3NGY2YjZiMmY=", "uniq": False},
    {"cn": "ED_UExVTUVfMDc1MjkxMUdfMV8xMDg0Mw==", "cv": "NjQ2ZDU1NDI1MTJiNzM3ODRhNDE3NDQ2NTI0YTU4NzY1NTRiNmM2MjM0NDE1NzU3NmYzNTQyNGY2ODUx", "uniq": False}
]

@app.route('/test_login')
def test_login():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # Version 4.98.0 comme le vrai navigateur
    session.get("https://api.ecoledirecte.com/v3/login.awp?gtk=1&v=4.98.0", headers=headers)
    login_data = {
        "identifiant": ED_USERNAME,
        "motdepasse": ED_PASSWORD,
        "isReLogin": False,
        "uuid": "",
        "fa": FA
    }
    payload = "data=" + quote(json.dumps(login_data))
    resp = session.post(
        "https://api.ecoledirecte.com/v3/login.awp?v=4.98.0",
        headers=headers,
        data=payload
    )
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
