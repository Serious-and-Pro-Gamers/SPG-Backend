from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})


@app.route("/")
def hello():
    return "<h1>Welcome to main page for the SeriousAndProGamers API v1.0! (Work In Progress...)</h1><br><p>Use the base url followed by <strong>/v1/&lt;route_path&gt;</strong> to test the API!<p><br><p>Use <strong>/v1</strong> to check the available routes</p>"


@app.route("/v1")
def avail_routes():
    return "<p>Available routes:<br> GET /ping -- sanity check endpoint</p>"


@app.route("/v1/ping")
def ping():
    return "pong!"


if __name__ == "__main__":
    # Since the host has a wildcard, use the respective urls for dev and prod
    app.run(host='0.0.0.0', debug=True)
