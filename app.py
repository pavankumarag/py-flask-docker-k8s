from flask import Flask

app = Flask(__name__)

@app.route('/new')
def hello():
    return "<h1>From flask</h1>"

@app.route('/new1')
def hello1():
    return "<h1>From flask new1</h1>"

@app.route('/new2')
def hello2():
    return "<h1>From flask new1</h1>"

if __name__ == "__main__":
    app.run(debug=True)