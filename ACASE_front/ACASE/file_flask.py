#!/usr/bin/python3
# coding=utf8
"""
starts a Flask web application
"""
import json
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

with open('results.json', 'r', encoding='utf-8') as f:
    obj = json.load(f)
    print(obj)


@app.route('/card', strict_slashes=False, methods=['GET'])
def index():
    """return object"""
    return json.dumps(obj)


@app.route('/keywords', strict_slashes=False, methods=['GET'])
def keyworkds():
    keywords_list = ['ciberseguridad', 'liderazgo', 'innovacion',
                     'innovation', 'leadership', 'security', 'management']
    return json.dumps(keywords_list)


@app.route('/target', strict_slashes=False, methods=['GET'])
def url():
    url_list = ['www.google.com', 'www.innovation_leadership.com', 'www.lamanzanainnovadora.com',
                'www.pepelinteligente.com', 'www.seguridadalmaximo.com', 'www.nevertrustanothers.com']
    return json.dumps(url_list)


@app.route('/form', strict_slashes=False, methods=['POST'])
def form():
    id = request.form['id']
    relevance = request.form['relevance']
    learning = request.form['learning']
    finding = request.form['finding']
    page = request.form['page']
    print(f'''
    id: {id}
    revelance: {relevance}
    learning: {learning}
    finding: {finding}
    page: {page}''')
    return 'Succesfully'


@app.route('/to_my_selection', strict_slashes=False, methods=['POST'])
def my_selection():
    id = int(json.loads(request.data)['id'])
    obj[id]['My_selection'] = True
    print(obj[id])
    return 'Succesfully'


@app.route('/to_trash', strict_slashes=False, methods=['POST'])
def to_trash():
    id = int(json.loads(request.data)['id']) - 1
    obj[id]['Trash_section'] = True
    return 'Successfully'


if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)
