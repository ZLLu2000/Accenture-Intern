#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import numpy as np
from flask import Flask, request
from flask import render_template
import pickle
app = Flask(__name__)

# 加载模型
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
@app.route('/index')
def hello():
    return render_template('input.html')

@app.route("/api/regression")
def getRgressionData():
    data1 = request.args.get("data1")
    data2 = request.args.get("data2")
    data3 = request.args.get("data3")
    data4 = request.args.get("data4")
    data5 = request.args.get("data5")
    data6 = request.args.get("data6")
    data7 = request.args.get("data7")
    data8 = request.args.get("data8")
    data9 = request.args.get("data9")

    data8_trans = {'CC': 0, 'EC': 1, 'EN': 2, 'NC': 3, 'SC': 4}
    data8 = data8_trans[data8]
    data9_trans = {'True': 1, 'False': 0}
    data9 = data9_trans[data9]

    data = [[data1, data2, data3, data4, data5, data6, data7, data8, data9]]

    predict = model.predict(np.array(data))
    output_data = {"data": predict[0]}
    output_data = json.dumps(output_data)
    output_data = json.loads(output_data)
    return render_template('output.html',data=output_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8888)
