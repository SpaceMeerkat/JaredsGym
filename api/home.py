from flask import (Blueprint,render_template, send_from_directory)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/", methods=None)
def home_landing():
    """ Handles the home landing page. All logic beyond the static html render
    should go into here """
    
    return send_from_directory('frontend/build','home.html')