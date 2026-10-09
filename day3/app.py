from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/home/')
def home():
    return f'Welcome to Day-3 learning about Static Vs Dynamic routes'
@app.route('/profile/')
def info():
    return f'Hello this is Manoj,traine at codegnan'
@app.route('/mahi')
def details():
    return f'Currently in flask class it is day3'
#Static routing ---> /name/saketh 
#dynamic routing ---> /namae/<name>
@app.route('/name/manoj') #static 
def data():
    return f'Welcome Manoj......'
@app.route('/name/<name>')
def student_name(name):
    return f'Hello {name}'
#Now we want to create related to course names
@app.route('/courses/<course_name>')
def courses(course_name):
    return f'<h1>This Course is :</h1><b>{course_name}</b>'

#Converters ---> int,str,float,path,uuid
#Integer converters 
@app.route('/student/<int:student_id>')
def studentid(student_id):
    return f'The ID od student is {student_id}'
#Float converters 
@app.route('/percentages/<float:percentage>')
def studentpercentages(percentage):
    return f'The Percentage of Student is {percentage}'
#Path Converters 
@app.route('/path/<path:file_path>')
def filepath(file_name):
    return f'The path is {file_name}'
#UUID ---> Universal Unique Identifier
@app.route('/student_id/<uuid:stu_id>')
def student_id(stu_id):
    return f'The Search for Student is {stu_id}'
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5002,debug=True,use_reloader=False)