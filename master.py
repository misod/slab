from flask import Flask
app = Flask("master")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<int:slave_id>/int:cpu>')
def get_info(slave_id, cpu):


    return "info recived"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
