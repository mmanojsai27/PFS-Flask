from flask import Flask,render_template,url_for,redirect,request
#create a flask application instance 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
    #return f'Flase Server is running'
#GET ---> fetching the data from db
#POST ----> Store the data in db,forms 
#PUT ----> Update the data 
@app.route('/getData',methods=['GET'])
def getData():
    name = request.args.get('name')
    email= request.args.get('email')
    return f'The name is {name} and email is {email}'

@app.route('/postdata',methods=['POST'])
def postdata():
    data = request.get_json()
    name = data['name']
    email = data['email']
    return f'the name is {name}, email is {email}'

@app.route('/postData',methods=['POST'])
def postData():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if name is None or len(name) < 5:
        return render_template('index.html',
                               err="Invaild name")
    if email is None:
        return render_template('index.html',
                                       err="Invaild email")
    if password is None or len(password) < 4:
        return render_template('index.html',
                                       err="Password is Error!")
    return render_template('index.html',
                                   msg="Successful")
@app.route('/updateData/<email>',methods=['PUT'])
def updateData(email):
    data = request.get_json()
    email1 = data['email']
    print(email1)
    #DATABASE LOGIC FOR PUT
    return f'Data is updated successfully for {email}'
@app.route('/deleteData/<email>',methods=['DELETE'])
def deleteData(email):
    #Database logic for delete
    return f'Data is deleted successfully for {email}'
@app.route('/register', methods=['GET', 'POST'])
def register():
#here we will mention our condition it can be
#either GET or POST
    if request.method == "GET":
        name = request.args.get('name')
    if request.method == "POST":
        data = request.get_json()
        #in POST method we will store the data in JSON
        name = data['name']
    return f'The name is {name}'

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5002,debug=True,use_reloader=False)