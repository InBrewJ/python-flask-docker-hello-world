from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def hello():
    return "Langford Lightning Talk"


@app.route("/feed", methods=["GET", "POST"])
@cross_origin()
def write_feed_time():
    if request.method == "GET":
        """return the last feed time from the file"""
        with open("./willow_fed_at.json", "r") as file:
            lines = [line.rstrip() for line in file]
        return str(lines)
    if request.method == "POST":
        """add the last timestamp to the file"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.json  # a multidict containing POST data
        to_write = {**data, "timestamp": datetime.now().isoformat()}
        app.logger.info("%s << POST data", str(to_write))
        with open("./willow_fed_at.json", "w") as f:
            f.write(str(to_write))
        return {"success": 1}
    else:
        # POST Error 405 Method Not Allowed
        print(f"langford: NOT A GET OR POST!")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4002))
    app.run(debug=True, host="0.0.0.0", port=port)
