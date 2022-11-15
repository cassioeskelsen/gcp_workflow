import functions_framework
from flask import jsonify

persons = {'123.123.123-13': {'name': 'cebolinha', 'score': 90},
           '124.124.124-14': {'name': 'monica', 'score': 60},
           '125.125.125-15': {'name': 'chico bento', 'score': 30}
           }


@functions_framework.http
def identify_person(request):
    request_json = request.get_json()

    # here we can make a identification with a biometry service using person photo.
    photo_id = request_json['photo_id']

    # but, isn't our focus here, make a simple check :)
    if request_json['person_id'] in persons:
        output = {'identified': True}
    else:
        output = {'identified': False}
    return jsonify(output)
