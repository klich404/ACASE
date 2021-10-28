#!/usr/bin/python3
"""
starts a Flask web application
"""
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/card', strict_slashes=False, methods= ['GET', 'POST'])
def index():
    """return object"""
    obj = [
        {
            'id': '01',
            'title': 'Desarrollo del Liderazgo, prioridad para el 74% de las empresas de AL',
            'url': 'http://www.google.com',
            'date': '04 Feb 2015',
            'text': 'El desarrollo de Liderazgo es prioridad en la agenda de la mayoría de las organizaciones de América Latina',
            'Associated_KW': 'emprendimiento',
            'My_selection': True,
            'Trash_section': False,
        },
        {
            'id': '02',
            'title': 'Jóvenes líderes globales de 2017',
            'url': 'http://www.our-thinking/career/asi-son-los-jovenes-lideres-globales-de-2017.html',
            'date': '13 Dec 2018',
            'text': 'Tienen menos de 40 años y destacan en campos tan diversos como la edición genética, el apoyo integral a zonas rurales o el liderazgo sustentable de  compañías.',
            'Associated_KW': 'banano',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '03',
            'title': 'Tendencias en la contratación de líderes 2019',
            'url': '/our-thinking/career/tendencias-en-la-contratacion-de-lideres-2019-mettl.html',
            'date': '03 Nov 2019',
            'text': 'Este informe aporta insights sobre las tendencias, desafíos y prácticas recomendadas en cuanto a liderazgo que las organizaciones de diferentes tamaños aplican.',
            'Associated_KW': 'innovacion',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '04',
            'title': 'Tendencias en la contratación de líderes 2019',
            'url': '/our-thinking/career/tendencias-en-la-contratacion-de-lideres-2019.html',
            'date': '03 Nov 2019',
            'text': 'Este informe aporta insights sobre las tendencias, desafíos y prácticas recomendadas en cuanto a liderazgo que las organizaciones de diferentes tamaños aplican.',
            'Associated_KW': 'management',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '05',
            'title': 'Destaca América Latina en la formación de líderes de negocio frente a Asia',
            'url': '/newsroom/destaca-america-latina-en-formacion-de-lideres-de-negocio-frente-asia.html',
            'date': '29 May 2020',
            'text': 'Estudio "Mejores Prácticas de Liderazgo", realizado entre 1,000 compañías de Latinoamérica, Asia Pacífico y Medio Oriente',
            'Associated_KW': 'liderazgo',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '06',
            'title': 'Desarrollo del Liderazgo, prioridad para el 74% de las empresas de AL',
            'url': '/newsroom/liderazgo-prioridad-para-el-74-porciento-de-las-empresas.html',
            'date': '04 Feb 2015',
            'text': 'El desarrollo de Liderazgo es prioridad en la agenda de la mayoría de las organizaciones de América Latina',
            'Associated_KW': 'tesito',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '07',
            'title': 'Jóvenes líderes globales de 2017',
            'url': '/our-thinking/career/asi-son-los-jovenes-lideres-globales-de-2017.html',
            'date': '13 Dec 2018',
            'text': 'Tienen menos de 40 años y destacan en campos tan diversos como la edición genética, el apoyo integral a zonas rurales o el liderazgo sustentable de  compañías.',
            'Associated_KW': 'asociacion',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '08',
            'title': 'Tendencias en la contratación de líderes 2019',
            'url': '/our-thinking/career/tendencias-en-la-contratacion-de-lideres-2019-mettl.html',
            'date': '03 Nov 2019',
            'text': 'Este informe aporta insights sobre las tendencias, desafíos y prácticas recomendadas en cuanto a liderazgo que las organizaciones de diferentes tamaños aplican a la venta de enseres de sueño que no sé y nbo se ajhdflasdjhlkasjhd',
            'Associated_KW': 'seguridad',
            'My_selection': False,
            'Trash_section': False,
        },
        {
            'id': '09',
            'title': 'Tendencias en la contratación de líderes 2019',
            'url': '/our-thinking/career/tendencias-en-la-contratacion-de-lideres-2019.html',
            'date': '03 Nov 2019',
            'text': 'Este informe aporta insights sobre las tendencias, desafíos y prácticas recomendadas en cuanto a liderazgo que las organizaciones de diferentes tamaños aplican.',
            'Associated_KW': 'leche',
            'My_selection': False,
            'Trash_section': True,
        },
        {
            'id': '10',
            'title': 'Destaca América Latina en la formación de líderes de negocio frente a Asia',
            'url': '/newsroom/destaca-america-latina-en-formacion-de-lideres-de-negocio-frente-asia.html',
            'date': '29 May 2020',
            'text': 'Estudio "Mejores Prácticas de Liderazgo", realizado entre 1,000 compañías de Latinoamérica, Asia Pacífico y Medio Oriente',
            'Associated_KW': 'aguacate',
            'My_selection': False,
            'Trash_section': True,
        }
]
    return json.dumps(obj)

@app.route('/keywords', strict_slashes=False)
def keyworkds():
    keywords_list = ['ciberseguridad', 'liderazgo', 'innovacion', 'innovation', 'leadership', 'security', 'management']
    return json.dumps(keywords_list)

@app.route('/target', strict_slashes=False)
def url():
    url_list = ['www.google.com', 'www.innovation_leadership.com', 'www.lamanzanainnovadora.com', 'www.pepelinteligente.com', 'www.seguridadalmaximo.com', 'www.nevertrustanothers.com']
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

@app.route('/my_selection', strict_slashes=False, methods=['POST'])
def my_selection():
    print(request.data)
    return 'Succesfully'

@app.route('/to_trash', strict_slashes=False, methods=['POST'])
def to_trash():
    print(request.data)
    return 'Successfully'

if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)