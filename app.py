from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? it\'s me, penguin!'

if __name__ == '__main__':
    app.run(debug=True)