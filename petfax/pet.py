from pathlib import Path
from flask import Blueprint, render_template
import json

bp = Blueprint('pet', __name__, url_prefix="/pets")

file = Path(__file__).with_name('pets.json')
pets = json.load(open(file))

@bp.route('/')
def index():
    return render_template('/pets/index.html', pets=pets)

@bp.route('/<index>')
def show_page(index):
    for i in pets:
        if str(i["pet_id"]) == index:
            return render_template('/pets/show.html', pet=i)
    return render_template('404.html')