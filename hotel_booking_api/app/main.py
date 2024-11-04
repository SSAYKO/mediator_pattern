from flask import jsonify, request
from . import app, booking_service

@app.route('/create_booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    booking_id = data.get('booking_id')
    user_data = data.get('user_data', {})
    result = booking_service.create_booking(booking_id, user_data)
    return jsonify(result)

@app.route('/cancel_booking', methods=['POST'])
def cancel_booking():
    data = request.get_json()
    booking_id = data.get('booking_id')
    result = booking_service.cancel_booking(booking_id)
    return jsonify(result)
