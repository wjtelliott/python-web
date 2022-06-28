from pathlib import Path
from flask import Blueprint, render_template
import json

bp = Blueprint('fact', __name__, url_prefix="/facts")

file = Path(__file__).with_name('facts.json')
pets = json.load(open(file))

@bp.route('/')
def index():
    # todo: fact index page
    return render_template('404.html')

@bp.route('/new')
def new_page():
    return render_template('fact_form.html')