import functions_framework
from flask import jsonify

persons = {'123.123.123-13': {'name': 'cebolinha', 'score': 90},
           '124.124.124-14': {'name': 'monica', 'score': 60},
           '125.125.125-15': {'name': 'chico bento', 'score': 30}
           }

houses = {'1': {'reserved': True, 'rented': False},
          '2': {'reserved': False, 'rented': False},
          '3': {'reserved': False, 'rented': True}
          }


@functions_framework.http
def reserve_house(request):
    request_json = request.get_json()
    person_id = request_json['person_id']
    house_id = request_json['house_id']
    if houses[house_id]['reserved'] is True or houses[house_id]['rented'] is True:
        output = {'result': False, 'message': 'House reserved or already rented'}
    else:
        output = {'result': True}
    return jsonify(output)
