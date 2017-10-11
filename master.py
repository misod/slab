from flask import Flask
app = Flask("master")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
