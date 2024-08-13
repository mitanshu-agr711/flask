from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/value/<int:score>')
def value(score):
     return "the value is: " + str(score)

if __name__ == '__main__':
    app.run(debug=True)
    