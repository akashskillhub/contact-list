from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"message":"Flask Server Running Successfully"}

@app.route("/me")
def home():
    return {"message":"john doe"}

if __name__ == "__main__":
    app.run(debug=True)