import urllib
from io import BytesIO

import requests
from flask import (Blueprint, current_app, jsonify, make_response,
                   render_template, request)

from .helpers import prepare_image_for_json

bp = Blueprint('routes', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@bp.route('/inpaint', methods=['GET', 'POST'])
def inpaint():
    if request.method == 'POST':
        prepared_image = prepare_image_for_json(request.files['image'])
        json = {'image': prepared_image}
        url = current_app.config.get('INPAINT_API_URL') + 'api/inpaint'
        api_response = requests.post(
            url, json=json, timeout=60)
        return make_response(jsonify(api_response.json()), 200)
    elif request.method == 'GET':
        return render_template('inpaint.html')


@bp.route('/cut', methods=['GET', 'POST'])
def cut():
    if request.method == 'POST':
        prepared_image = prepare_image_for_json(request.files['image'])
        json = {'image': prepared_image}
        url = current_app.config.get('INPAINT_API_URL') + 'api/cut'
        api_response = requests.post(
            url, json=json, timeout=60)
        return make_response(jsonify(api_response.json()), 200)
    elif request.method == 'GET':
        return render_template('cut.html')


@bp.route('/mask', methods=['GET', 'POST'])
def mask():
    if request.method == 'POST':
        prepared_image = prepare_image_for_json(request.files['image'])
        json = {'image': prepared_image}
        url = current_app.config.get('INPAINT_API_URL') + 'api/mask'
        api_response = requests.post(
            url, json=json, timeout=60)
        return make_response(jsonify(api_response.json()), 200)
    elif request.method == 'GET':
        return render_template('mask.html')
