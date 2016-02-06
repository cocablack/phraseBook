from flask import Flask, request, jsonify
from json import dumps

import os
import sys
sys.path.append(os.getcwd())
import sentiment

app = Flask(__name__, static_url_path='/static')
app.debug = True

@app.route('/query', methods=['GET', 'POST'])
def query():
    print("[/query]")
    
    req = request.get_json(force=True)
    print(req)
    
    result = sentiment.query(req)
    
    return dumps(result)
    
if __name__ == "__main__":
    sentiment.load_database()
    app.run(host="localhost", port=8080)