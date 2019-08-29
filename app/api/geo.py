from . import api
from flask import jsonify


@api.route('/geo', methods=['GET'])
def get_satelite_citys():
    """
    Recupera informações sobre as organizações
    ---
    default: all
    responses:
      200:
        description: Recupera os dados das organizações
    """
    data = [
        {
            "pk": 1,
            "fields": {
                "name": "Plano Piloto",
                "number": "I",
                "uf": "DF"
            }
        },
        {
            "pk": 2,
            "fields": {
                "name": "Gama",
                "number": "II",
                "uf": "DF"
            }
        },
        {
            "pk": 3,
            "fields": {
                "name": "Taguatinga",
                "number": "III",
                "uf": "DF"
            }
        },
        {
            "pk": 4,
            "fields": {
                "name": "Brazlândia",
                "number": "IV",
                "uf": "DF"
            }
        },
        {
            "pk": 5,
            "fields": {
                "name": "Sobradinho",
                "number": "V",
                "uf": "DF"
            }
        },
        {
            "pk": 6,
            "fields": {
                "name": "Planaltina",
                "number": "VI",
                "uf": "DF"
            }
        },
        {
            "pk": 7,
            "fields": {
                "name": "Paranoá",
                "number": "VII",
                "uf": "DF"
            }
        },
        {
            "pk": 8,
            "fields": {
                "name": "Núcleo Bandeirante",
                "number": "VIII",
                "uf": "DF"
            }
        },
        {
            "pk": 9,
            "fields": {
                "name": "Ceilândia",
                "number": "IX",
                "uf": "DF"
            }
        },
        {
            "pk": 10,
            "fields": {
                "name": "Guará",
                "number": "X",
                "uf": "DF"
            }
        },
        {
            "pk": 11,
            "fields": {
                "name": "Cruzeiro",
                "number": "XI",
                "uf": "DF"
            }
        },
        {
            "pk": 12,
            "fields": {
                "name": "Samambaia",
                "number": "XII",
                "uf": "DF"
            }
        },
        {
            "pk": 13,
            "fields": {
                "name": "Santa Maria",
                "number": "XIII",
                "uf": "DF"
            }
        },
        {
            "pk": 14,
            "fields": {
                "name": "São Sebastião",
                "number": "XIV",
                "uf": "DF"
            }
        },
        {
            "pk": 15,
            "fields": {
                "name": "Recanto das Emas",
                "number": "XV",
                "uf": "DF"
            }
        },
        {
            "pk": 16,
            "fields": {
                "name": "Lago Sul",
                "number": "XVI",
                "uf": "DF"
            }
        },
        {
            "pk": 17,
            "fields": {
                "name": "Riacho Fundo",
                "number": "XVII",
                "uf": "DF"
            }
        },
        {
            "pk": 18,
            "fields": {
                "name": "Lago Norte",
                "number": "XVIII",
                "uf": "DF"
            }
        },
        {
            "pk": 19,
            "fields": {
                "name": "Candagolândia",
                "number": "XIX",
                "uf": "DF"
            }
        },
        {
            "pk": 20,
            "fields": {
                "name": "Águas Claras",
                "number": "XX",
                "uf": "DF"
            }
        },
        {
            "pk": 21,
            "fields": {
                "name": "Riacho Fundo II",
                "number": "XXI",
                "uf": "DF"
            }
        },
        {
            "pk": 22,
            "fields": {
                "name": "Sudoeste/Octogonal",
                "number": "XXII",
                "uf": "DF"
            }
        },
        {
            "pk": 23,
            "fields": {
                "name": "Varjão",
                "number": "XXIII",
                "uf": "DF"
            }
        },
        {
            "pk": 24,
            "fields": {
                "name": "Park Way",
                "number": "XXIV",
                "uf": "DF"
            }
        },
        {
            "pk": 25,
            "fields": {
                "name": "SCIA",
                "number": "XXV",
                "uf": "DF"
            }
        },
        {
            "pk": 26,
            "fields": {
                "name": "Sobradinho II",
                "number": "XXVI",
                "uf": "DF"
            }
        },
        {
            "pk": 27,
            "fields": {
                "name": "Jardim Botânico",
                "number": "XXVII",
                "uf": "DF"
            }
        },
        {
            "pk": 28,
            "fields": {
                "name": "Itapoã",
                "number": "XXVIII",
                "uf": "DF"
            }
        },
        {
            "pk": 29,
            "fields": {
                "name": "SIA",
                "number": "XXIX",
                "uf": "DF"
            }
        },
        {
            "pk": 30,
            "fields": {
                "name": "Vicente Pires",
                "number": "XXX",
                "uf": "DF"
            }
        },
        {
            "pk": 31,
            "fields": {
                "name": "Fercal",
                "number": "XXXI",
                "uf": "DF"
            }
        }
    ]
    return jsonify(data)
