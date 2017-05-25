from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def helloworld():
    return render_template('home.html')
@app.route('/signin', methods=['GET'])
def signin_form():
    username='pxg'
    return render_template('form.html',username=username,)

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
   # if username=='admin' and password=='password':
       # return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if  __name__=='__main__':
    app.run()

app.run(host='127.0.0.1',port='5000')