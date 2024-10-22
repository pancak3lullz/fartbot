from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# List of calming YouTube videos
videos = [
    "https://www.youtube.com/watch?v=2sPpWAzJfrg",  # Forest sounds
    "https://www.youtube.com/watch?v=WUXEeAXywCY",  # Ocean waves
    "https://www.youtube.com/watch?v=lM02vNMRRB0",  # River stream
    "https://www.youtube.com/watch?v=1ZYbU82GVz4",  # Rain
    "https://www.youtube.com/watch?v=5qap5aO4i9A"   # Lo-fi music
]

@app.route('/fart', methods=['POST'])
def fart():
    # Select a random video from the list
    video = random.choice(videos)

    # Prepare the Slack message response
    response = {
        "response_type": "in_channel",  # Visible to everyone
        "text": f"[💩]({video})"
    }
    return jsonify(response)

# Run the app (Render will assign the port automatically)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
