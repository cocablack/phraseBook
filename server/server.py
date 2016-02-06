from flask import Flask, request

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route('/query', methods=['GET', 'POST'])
def hello():
    return "Hello World!"
    
if __name__ == "__main__":
    app.run(host="localhost", port=8080)