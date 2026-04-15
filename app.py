from flask import Flask, Response
import requests

app = Flask(__name__)

SOURCE_URL = "https://raw.githubusercontent.com/Shihaix/Pluto-TV-Playlists/main/output/plutotv_us.m3u8"

@app.route("/")
def playlist():
    try:
        res = requests.get(SOURCE_URL)
        res.raise_for_status()
        lines = res.text.splitlines()

        output = ["#EXTM3U"]

        for i in range(len(lines)):
            line = lines[i]

            # ✅ TEMP: NO FILTER (debug mode)
            if line.startswith("#EXTINF"):
                output.append(line)
                if i + 1 < len(lines):
                    output.append(lines[i+1])

        return Response("\n".join(output), mimetype="text/plain")

    except Exception as e:
        return f"ERROR: {str(e)}"
