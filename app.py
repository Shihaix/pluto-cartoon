from flask import Flask, Response
import requests

app = Flask(__name__)

SOURCE_URL = "https://raw.githubusercontent.com/Shihaix/Pluto-TV-Playlists/main/output/plutotv_us.m3u8"
CHANNEL_ID = "6675c7868768aa0008d7f1c7"

@app.route("/")
def playlist():
    try:
        res = requests.get(SOURCE_URL, timeout=10)
        res.raise_for_status()
        lines = res.text.splitlines()

        output = ["#EXTM3U"]

        for i in range(len(lines)):
            line = lines[i]

            if line.startswith("#EXTINF") and CHANNEL_ID in line:
                output.append(line)
                if i + 1 < len(lines):
                    output.append(lines[i+1])
                break  # only one channel

        return Response("\n".join(output), mimetype="text/plain")

    except Exception as e:
        return f"Error: {str(e)}"
