import functions_framework
from flask import jsonify

persons = {'123.123.123-13': {'name': 'cebolinha', 'score': 90},
           '124.124.124-14': {'name': 'monica', 'score': 60},
           '125.125.125-15': {'name': 'chico bento', 'score': 30}
           }


@functions_framework.http
def score_person(request):
    request_json = request.get_json()
    output = {'score': persons[request_json['person_id']]['score']}
    return jsonify(output)
