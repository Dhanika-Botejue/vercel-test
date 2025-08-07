from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World - This is a test to know how to deploy with vercel"

if __name__ == "__main__":
    app.run()