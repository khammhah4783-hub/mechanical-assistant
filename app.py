import math
import json
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print("=" * 60)
    print("  ⚙️  Mechanical Engineering Assistant")
    print("  Open: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000)