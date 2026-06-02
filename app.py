from flask import Flask, redirect

app = Flask(__name__)

BASE_URL = "https://raw.githubusercontent.com/Shihaix/Pluto-TV-Playlists/main/output/plutotv_us.m3u8"


@app.route("/")
def home():
    return "Pluto Proxy OK"


@app.route("/channel/<channel_id>")
def channel(channel_id):
    try:
        import requests

        r = requests.get(BASE_URL, timeout=15)
        lines = r.text.splitlines()

        for i in range(len(lines)):
            if channel_id in lines[i]:
                stream_url = lines[i + 1]

                # 🔥 IMPORTANT: redirect terus (OTT friendly)
                return redirect(stream_url)

        return "Channel not found", 404

    except Exception as e:
        return str(e), 500
