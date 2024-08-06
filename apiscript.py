from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('new.html')

@app.route('/haveData')
def getData():
    return 'Welcome to thi'

if __name__=='__main__':
    app.run(debug=True)