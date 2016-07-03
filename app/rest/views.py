from flask import jsonify

from .import rest


@rest.route('/', methods=['GET'])
def rest_start():
    return jsonify({'message': 'try to be restful!'})
