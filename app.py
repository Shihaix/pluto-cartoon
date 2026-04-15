@app.route("/")
def stream_only():
    try:
        res = requests.get(SOURCE_URL, timeout=10)
        res.raise_for_status()
        lines = res.text.splitlines()

        for i in range(len(lines)):
            if lines[i].startswith("#EXTINF") and CHANNEL_ID in lines[i]:
                stream_url = lines[i+1]

                stream = requests.get(stream_url, stream=True)
                return Response(
                    stream.iter_content(chunk_size=1024),
                    content_type=stream.headers.get("Content-Type", "application/vnd.apple.mpegurl")
                )

        return "Channel not found"

    except Exception as e:
        return f"Error: {str(e)}"
