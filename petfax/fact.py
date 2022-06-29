from pathlib import Path
from flask import Blueprint, redirect, render_template, request
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")

file = Path(__file__).with_name('facts.json')
pets = json.load(open(file))

@bp.route('/', methods=['POST', 'GET'])
def index():
    # todo: fact index page
    if request.method == 'GET': return render_template('/facts/index.html')

    return redirect('/facts/')

@bp.route('/new')
def new_page():
    return render_template('/facts/new.html')