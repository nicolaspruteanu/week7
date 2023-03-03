from flask import Blueprint, request

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.get('/noc')
@bp.get('/noc/<code>')
def noc_get(code=None):
    """Returns a list of NOC codes with the country/region name and notes or if a code is passed then returns the details for that code """
    if code:
        return f"The details for {code}."
    else:
        return "Returns a list of NOC codes"

@bp.post('/noc')
@bp.patch('/noc/<code>')
@bp.delete('/noc/<code>')
def create_update_noc(code=None):
    if request.method == "PATCH":
        return f"The updated details for {code}"
    elif request.method == "GET":
        return "The record was successfully created.", 201
    elif request.method == "DELETE":
        return "The record was successfully deleted", 202

