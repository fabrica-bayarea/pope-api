from . import api
from flask import jsonify


@api.route('/organizations', methods=['GET'])
def get_organizations():
    """
    Recupera informações sobre as organizações
    ---
    default: all
    responses:
      200:
        description: Recupera os dados das organizações
    """
    data = {
        'name': 'Cartorio da ceilândia',
        'tell': '(61) 3333 - 3333',
        'email': 'cartorio@gmail.com',
        'address': 'QNN 23 cj j casa 3',
        'city': 'Ceilândia',
        'description': 'Cartório e talz',
        'free': 0,
        'area': 'Jurídica',
        'id_sub_area': 'Cartórios',
        'attendance': {
            'seg': '8 as 18h',
            'ter': '8 as 18h',
            'qua': '8 as 18h',
            'qui': '8 as 18h',
            'sex': '8 as 18h',
            'sab': '8 as 18h',
            'dom': '8 as 18h',
        },
    }
    return jsonify(data)
