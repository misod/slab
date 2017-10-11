from flask import Flask
app = Flask("master")

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post/<int:slave_id>/<cpu>')
def get_info(slave_id, sl_id):
    print slave_id
    print cpu

# @app.route('/post/<int>/<int:slave_id>')
# def get_info(slave_id):
#     print slave_id
#     #print cpu

    return "info recived \n"

if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True)
