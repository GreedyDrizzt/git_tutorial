from flask import Flask,abort,redirect,url_for,render_template,request

app = Flask(__name__)
app.config['USENAME'] = "hello"
app.config['PASSWORD'] = "world"
app.secret_key = 'haha'

@app.route('/')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', tpl_name=username)

@app.route('/goodbye')
def bye():
    return "goodbye!"

@app.route('/login',methods=["GET"])
def login_get():
     return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_post():
     if request.form['username'] !=app.config['USENAME']:
      return 'Invalid username'
     elif request.form['passwd'] !=app.config['PASSWORD']:
         return "Invalid password"
     else:
         return "You were looged in"
if __name__ == '__main__':
    app.run(port=5050,debug=True)