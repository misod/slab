from flask import Flask, jsonify
app = Flask("master")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/slave/<int:slave_id>')
def get_info(slave_id):
    print slave_id

    return "info recived \n"

@app.route('/slave/<int:slave_id>/<int:cpu>')
def get_info_cpu(slave_id, cpu):
    print slave_id
    print cpu

    return jsonify("yheee")

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
