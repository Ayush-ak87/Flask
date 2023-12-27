##jinja2 template engine
'''
{%...%} for statements
{{     }} expression to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app =Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/members')
def members():
    return "Welcome to Flask Members."

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"
    exp={'score':score,'res':res}
    return render_template('result.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    return "Failed with a score of "+ str(score)

@app.route('/results/<int:marks>')
def results(marks):
    results=""
    if marks<50:
        results='fail'
    else:
        results='success'
    return redirect(url_for(results,score=marks))

## Result Checker Submit Form
@app.route('/submit',methods={'POST','GET'})
def submit():
    total_score = 0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    res=""
    return redirect(url_for('success',score=total_score))

if __name__=='__main__':
    app.run()