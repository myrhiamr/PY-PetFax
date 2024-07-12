
from flask import ( Blueprint, render_template )
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

# specific pet view route
@bp.route('/<int:id>')
def show(id):
    with open('pets.json', 'r', encoding='utf-8') as f:
        pets = json.load(f)
    pet = pets[id - 1]
    return render_template('pets/show.html', pet=pet)
