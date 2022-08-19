import imp
from flask import Blueprint, request, jsonify
from currency_conv import CurrencyConverter

api = Blueprint('api', __name__)

converter = CurrencyConverter()

@api.route('/api/currencies', methods=['GET'])
def get_currencies():
    symbols = converter.fetchAllSymbols()

    if symbols is None:
        return jsonify({'error': 'Symbols not found'}), 404

    return jsonify(symbols), 200

@api.route('/api/convert/<frm>/<to>/<amt>', methods=['GET'])
def convert(frm, to, amt):
    converter.setBaseCurr(frm)
    result = converter.convert(amt, to)
    if result is None or len(result) == 0:
        return jsonify({'error': 'Conversion problem'}), 404

    return jsonify(result), 200

