import functions_framework
from flask import jsonify

persons = {'123.123.123-13': {'name': 'cebolinha', 'score': 90},
           '124.124.124-14': {'name': 'monica', 'score': 60}
           }


@functions_framework.http
def check_person_exists(request):
    request_json = request.get_json()
    if request_json['person_id'] in persons:
        output = {'person_exists': True}
    else:
        output = {'person_exists': False}
    return jsonify(output)
