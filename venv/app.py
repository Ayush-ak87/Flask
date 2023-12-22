from flask import Flask,redirect,url_for

app =Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask Code..."

@app.route('/members')
def members():
    return "Welcome to Flask Members."

@app.route('/success/<int:score>')
def success(score):
    return "Passed with a score of "+ str(score)

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

if __name__=='__main__':
    app.run(debug=True)