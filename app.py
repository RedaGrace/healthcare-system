from flask import *
import pandas as pd
import json, time
import pickle
import re
import os
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def home_page():
    return render_template('index.html')
    
@app.route('/symptoms_checker')   
def symptoms_checker_page():
    return render_template('symptoms.html')

@app.route('/first_aid')
def first_aid_page():
    return render_template('first_aid.html')

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
