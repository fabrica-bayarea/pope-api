from . import api
from flask import jsonify


@api.route('/organizations', methods=['GET'])
def get_example():
    """
    Recupera informações sobre as organizações
    ---
    default: all
    responses:
      200:
        description: Recupera os dados das organizações
    """
    data = {
        'teste': 'teste'
    }
    return jsonify(data)
