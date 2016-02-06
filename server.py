from flask import Flask, request, jsonify
from json import dumps

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route('/query', methods=['GET', 'POST'])
def query():
    print("[/query]")
    
    blah = request.get_json(force=True)
    print(blah)
    
    result = {}
    result["data"] = "hello world"
    
    return dumps(result)
    
if __name__ == "__main__":
    app.run(host="localhost", port=8080)