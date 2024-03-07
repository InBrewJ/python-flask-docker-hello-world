from flask import Flask
from flask import request
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Langford Lightning Talk"


@app.route("/feed", methods=["GET", "POST"])
def write_feed_time():
    if request.method == "GET":
        """return the last feed time from the file"""
        return {}
    if request.method == "POST":
        """add the last timestamp to the file"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form  # a multidict containing POST data
        print(data)
    else:
        # POST Error 405 Method Not Allowed
        print(f"langford: NOT A GET OR POST!")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
