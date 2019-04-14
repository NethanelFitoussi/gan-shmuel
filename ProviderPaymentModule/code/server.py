from flask import Flask
from flask import render_template
from flask import send_file
import os.path
from time import gmtime, strftime
from flask import request

app = Flask(__name__)


@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)