from flask import Flask,render_template,url_for,redirect,request
import uuid
app = Flask(__name__)
#We will generate UUID using python module 
@app.route('/')
def home():
    return redirect(url_for('indexpage'))
    #return "Welcome to Day-4 learning"
@app.route('/generate')
def generate():
    id = uuid.uuid4().hex
    print(id)
    return f'The generate id is:{id}'
@app.route('/index')
def indexpage():
    return render_template('index.html')
@app.route('/about')
def aboutpage():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port= 5001,debug=True,use_reloader=False)