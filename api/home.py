from flask import (Blueprint,render_template)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route("/", methods=None)
def home_landing():
    """ Handles the home landing page. All logic beyond the static html render
    should go into here """
    
    return render_template('home.html')