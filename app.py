from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,gttytyrgrgrf World!'

@app.route('/value/<int:score>')
def value(score):
     return "the value is: " + str(score)

if __name__ == '__main__':
    app.run(debug=True)
    