from flask import (
    Blueprint,
    request,
    jsonify,
    abort
)
from app_config import db
from models import Proficiency
from util import all_as_list_of_dicts, cPrint, simpleMsgResp


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def index():
    """
    Api root. Returns that it works.
    """
    return jsonify(simpleMsgResp('It works!'))


@api.route('/addProficiency', methods=["POST"])
def addProf():
    """
    Add a single proficiency.

    Query params expected:
    1. category
    2. label
    3. description
    4. rating

    Optional params:
    1. icon
    2. iconColour
    """

    expectedParams = ['category', 'label', 'description', 'rating']
    optionalParams = ['icon', 'iconColour']

    if not all(request.json.get(item) for item in expectedParams):
        return abort(400)

    json = request.json
    prof = Proficiency(
        category=json.get('category'),
        icon=json.get('icon') if json.get('icon') else None,
        iconColour=json.get('iconColour') if json.get('iconColour') else None,
        label=json.get('label'),
        description=json.get('description'),
        rating=json.get('rating')
    )

    try:
        db.session.add(prof)
        db.session.commit()
    except:
        db.session.rollback()
        return abort(500)

    db.session.close()
    return jsonify(simpleMsgResp("Your record has been sucesfully inserted."))


@ api.route('/getProficiencies')
def getAllProfs():
    """
    Returns all proficiencies.
    """
    all_results = Proficiency.query.all()
    as_dicts = all_as_list_of_dicts(all_results)
    cPrint(as_dicts)

    return jsonify(as_dicts)
