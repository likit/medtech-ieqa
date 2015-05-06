from Flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
