from flask import Flask
#Create a flask applications instance 
app = Flask(__name__)
#Now we will start defining the routes 
@app.route('/')
def home():
    """Default home page"""
    return "Hello guys how are you!"
@app.route('/manoj')
def details():
    """Details about manoj"""
    return "Manoj is trainer at codegnan and focusing on placement"
@app.route('/profile')
def info():
    """Details about profile"""
    return str({"Name: Manoj-sai", "role : Traine","subject :PFS"})

if __name__ == "__main__":
    #if port is alredy in use change the port numbers
    app.run(host='0.0.0.0',
            port=5700,debug=True)
