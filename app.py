@app.route("/Pokémon")
def spotlight():
    CHANNEL_ID = "6675c7868768aa0008d7f1c7"

    r = requests.get(SOURCE_URL, timeout=15)
    lines = r.text.splitlines()

    for i in range(len(lines)):
        if CHANNEL_ID in lines[i]:
            stream_url = lines[i + 1]

            stream = requests.get(
                stream_url,
                stream=True,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            return Response(
                stream.iter_content(chunk_size=8192),
                content_type=stream.headers.get(
                    "Content-Type",
                    "application/vnd.apple.mpegurl"
                ),
                direct_passthrough=True
            )

    return "Channel not found", 404
