#   Copyright 2017 Amazon.com, Inc. or its affiliates.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)

cors = CORS(app)
@app.route('/web', methods = ['GET', 'POST'])
def hello_world():    
    if request.method == 'POST':
        'r = requests.get('http://api2.python-flask-copilot.local:8000?ID=1')

         r =requests.get('http://localhost:8000/api')

        #return jsonify(response =r.text)
        return r.text
    else:
        print('inside GET')
        return render_template("index.html")



    
    # return ('<html>hi!  i\'m served via Python + Flask.  i\'m a web endpoint.</html>')
    


if __name__ == '__main__':
    app.run(port=3000,host='0.0.0.0')
