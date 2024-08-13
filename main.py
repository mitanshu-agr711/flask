from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/evaluated/<int:score>')
def evaluated(score):
    res = "pass" if score > 50 else "fail"
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return redirect(url_for('value',score=score))

@app.route('/result/<int:score>')
def result(score):
    result=""
    if score<50:
        result="fail"
    else:
        result="pass"
    return redirect(url_for('value',score=score))

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        english=float(request.form['english'])
        total_score=(science+maths+english)/3
        # return redirect(url_for('value',score=total_score))
        #  res=""
        return redirect(url_for('evaluated',score=total_score))
if __name__ == '__main__':  
    app.run(debug=True)
    