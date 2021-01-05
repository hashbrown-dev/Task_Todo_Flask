from flask import Blueprint, render_template

index_bp = Blueprint('index_bp', __name__, url_prefix='/home', template_folder='templates', static_folder='static')


@index_bp.route('/index')
def index():
    print("inside index function")
    return render_template('index.html')
