from flask import Flask, render_template, request, jsonify
from collections import defaultdict

app = Flask(__name__, template_folder="templates")


# in memory db
channelsDict = {
    "channel1": [
        {
            "display_name": "user1",
            "message": "hello world",
            "timestamp": "2021-01-01 00:00:00",
        }
    ],
    "channel2": [],
}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route(
    "/chat/start",
)
def chat_start():
    return render_template("chat_start.html")


@app.route("/channels")
def channels():
    return render_template("inside_chat/channels.html", channels=channelsDict.keys())


@app.route("/create-channel", methods=["POST"])
def create_channel():
    channel_name = request.json["channel_name"]
    if channel_name in channelsDict:
        return jsonify({"success": False, "error": "Channel already exists"})

    channelsDict[channel_name] = []
    return jsonify({"success": True, "channel_name": channel_name})


@app.route("/channels/<channel_name>")
def chat(channel_name):
    if channel_name not in channelsDict:
        return jsonify({"success": False, "error": "Channel does not exist"})

    messages = channelsDict[channel_name]
    return render_template(
        "inside_chat/chat.html", channel_name=channel_name, messages=messages
    )


# @app.route("/join-channel", methods=["POST"])
# def join_channel():
#     channel_name = request.form["channel_name"]
#     if channel_name not in channelsDict:
#         return jsonify({"success": False, "error": "Channel does not exist"})

#     return jsonify({"success": True, "channel_name": channel_name})


# if __name__ == "__main__":
#     app.run()
