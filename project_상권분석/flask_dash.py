#Module Name : lec_flask_test.py
import numpy as np
import matplotlib.pyplot as plt
import requests
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import pandas as pd
import cx_Oracle
import sqlalchemy

pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)

engine = sqlalchemy.create_engine('oracle://project:0000@localhost:1521/XE')
connect = engine.connect()

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# static    : 정적(css img js..)
# templates : 디자인(html)




# @app.route('/')
# def dash():
#     bd = '발달상권'
#     gm = '골목상권'
#     jt = '전통시장'
#     kk = '관광특구'
#     year = ['2019', '2020']
#     return render_template('dash.html',bd=bd,gm=gm,jt=jt,kk=kk)
#
# @app.route('/')
# def sg_jt():
#     bd = '발달상권'
#     gm = '골목상권'
#     jt = '전통시장'
#     kk = '관광특구'
#     year = ['2019', '2020']
#     return render_template('sg_jt.html',bd=bd,gm=gm,jt=jt,kk=kk)

@app.route('/')
def sg_kk():
    bd = '발달상권'
    gm = '골목상권'
    jt = '전통시장'
    kk = '관광특구'
    year = ['2019', '2020']
    return render_template('sg_kk.html',bd=bd,gm=gm,jt=jt,kk=kk)




# @app.route('/')
# def sg_bd():
#     bd = '발달상권'
#     gm = '골목상권'
#     jt = '전통시장'
#     kk = '관광특구'
#
#     return render_template('sg_bd.html',bd=bd,gm=gm,jt=jt,kk=kk)



@app.route('/info')
def info():
    return 'Info'

if __name__ == '__main__':
    app.run(host='localhost',port=8887,debug=True)
