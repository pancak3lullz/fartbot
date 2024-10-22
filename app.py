from flask import Flask, request, jsonify
import random, os

app = Flask(__name__)

# List of calming YouTube videos
videos = [
    "https://www.youtube.com/watch?v=2sPpWAzJfrg",  # Forest
    "https://www.youtube.com/watch?v=WUXEeAXywCY",  # Ocean waves
    "https://www.youtube.com/watch?v=lM02vNMRRB0",  # River stream
    "https://www.youtube.com/watch?v=1ZYbU82GVz4",  # Rain
    "https://www.youtube.com/watch?v=5qap5aO4i9A"   # Lo-fi stream
]

@app.route('/fart', methods=['POST'])
def fart():
    video = random.choice(videos)  # Pick a random video
    response = {
        "response_type": "in_channel",  # Make it visible to everyone
        "text": f"[💩]({video})"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
