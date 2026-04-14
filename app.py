from flask import Flask, Response
import requests

app = Flask(__name__)

SOURCE_URL = "https://raw.githubusercontent.com/Shihaix/Pluto-TV-Playlists/main/output/plutotv_us.m3u8"

KEYWORDS = ["Kids"]

@app.route("/")
def kids_playlist():
    text = requests.get(SOURCE_URL).text.splitlines()

    output = ["#EXTM3U"]

    for i in range(len(text)):
        line = text[i]
        if line.startswith("#EXTINF") and (
    'group-title="Kids"' in line or
    'cartoon' in line.lower() or
    'anime' in line.lower()
):
            output.append(line)
            if i + 1 < len(text):
                output.append(text[i+1])

    return Response("\n".join(output), mimetype="text/plain")
