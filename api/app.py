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

import boto3
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request


app = Flask(__name__)
cors = CORS(app)



@app.route('/api')

def hello_world():
    querystring = request.args.get("ID", "")
    querystring1 = int(querystring)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('python-flask-copilot-test-api2-countries')


    response = table.get_item(
        Key={
            'CountryId': querystring1
            }
                )
    item = response['Item']
    countryname=item['CountryName']            
    return jsonify(country =countryname)


if __name__ == '__main__':
    app.run(port=8000,host='0.0.0.0')
