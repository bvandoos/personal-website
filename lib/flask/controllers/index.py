from flask import Blueprint, render_template


index = Blueprint('index', __name__, url_prefix='/')


@index.route('/', methods=['GET', 'POST'])
def index_load():
    """

    """

    return render_template("index.html")