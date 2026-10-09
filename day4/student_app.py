from flask import Flask
import uuid
app = Flask(__name__)
@app.route('/')
@app.route('/studentpage')
def page():
    return "<b>----Welcome to Student Page----------</b>"
@app.route('/student/<int:stuid>')
def stdid(stuid):
    return f'The Student ID is : {stuid}'
@app.route('/attendance/<float:st_attendance>')
def stu_att(st_attendance):
    return f'The attendance of Student is {st_attendance}'
@app.route('/skills/<s1>/<s2>')
def skills(s1,s2):
    return f'Student has {s1} and {s2} skill set'
@app.route('/details/<path:file_path>')
def details(file_path):
    return f'The Path is {file_path}'
@app.route('/generate')
def generate():
    id = uuid.uuid3().hex
    return f'The Student search id is: {id}'
if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port= 5001,debug=True,use_reloader=False)