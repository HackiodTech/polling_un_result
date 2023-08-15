from flask import flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my flask App!'

if __name__ == '__main__':
    app.run(debug=True)
