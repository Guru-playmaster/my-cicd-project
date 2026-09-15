from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>My CI/CD Project yes</h1>
    <p>Hello! My first DevOps application is running.Guru kasi</p>
    <p>Version: 2.0</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)