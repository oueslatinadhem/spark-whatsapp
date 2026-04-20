from flask import Flask, jsonify
import requests
import json
import os
from urllib.parse import quote

app = Flask(__name__)

ED_USERNAME = os.environ.get("ED_USERNAME")
ED_PASSWORD = os.environ.get("ED_PASSWORD")
ED_CN = os.environ.get("ED_CN", "")
ED_CV = os.environ.get("ED_CV", "")
ED_CN2 = os.environ.get("ED_CN2", "")
ED_CV2 = os.environ.get("ED_CV2", "")

@app.route('/test_login')
def test_login():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    gtk_resp = session.get("https://api.ecoledirecte.com/v3/login.awp?gtk=1&v=4.75.0", headers=headers)
    gtk_cookie = gtk_resp.cookies.get("GTK", "")

    login_data = {
        "identifiant": ED_USERNAME,
        "motdepasse": ED_PASSWORD,
        "isRelogin": False,
        "uuid": ""
    }
    if ED_CN and ED_CV:
        login_data["fa"] = [
            {"cn": ED_CN, "cv": ED_CV},
            {"cn": ED_CN2, "cv": ED_CV2}
        ]

    payload = "data=" + quote(json.dumps(login_data))
    resp = session.post(
        "https://api.ecoledirecte.com/v3/login.awp?v=4.75.0",
        headers={**headers, "X-Gtk": gtk_cookie},
        data=payload
    )
    result = resp.json()
    return jsonify({"code": result.get("code"), "message": result.get("message", "")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
