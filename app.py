from flask import Flask, request, jsonify
import random, os

app = Flask(__name__)

# List of calming YouTube videos
videos = [
    "https://www.youtube.com/watch?v=2sPpWAzJfrg",  # Forest sounds
    "https://www.youtube.com/watch?v=WUXEeAXywCY",  # Ocean waves
    "https://www.youtube.com/watch?v=lM02vNMRRB0",  # River stream
    "https://www.youtube.com/watch?v=1ZYbU82GVz4",  # Rain
    "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lo-fi stream
    "https://www.youtube.com/watch?v=b5qHZ8LWzCQ",  # Fireplace sounds
    "https://www.youtube.com/watch?v=f77SKdyn-1Y",  # Relaxing piano music
    "https://www.youtube.com/watch?v=0EWbonj7f18",  # Wind blowing through trees
    "https://www.youtube.com/watch?v=WB-y7_ymPJ4",  # Bird sounds in the forest
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ"   
]


@app.route('/fart', methods=['POST'])
def fart():
    video = random.choice(videos)  # Pick a random video
    response = {
        "response_type": "in_channel",
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"<{video}|💩 go touch grass>"
                }
            }
        ]
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
