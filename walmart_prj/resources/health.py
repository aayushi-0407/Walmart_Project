from flask import Blueprint, request, jsonify, session
from models.users import User
from utils import calculate_bmi, suggest_food

health_bp = Blueprint('health', __name__)

@health_bp.route('/bmi', methods=['POST'])
def calculate_and_suggest():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 401

    user = User.query.filter_by(username=session['username']).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404

    height = user.height
    weight = user.weight

    if not height or not weight:
        return jsonify({'message': 'Height and weight are required in profile'}), 400

    try:
        bmi = calculate_bmi(height, weight)
        suggestions = suggest_food(bmi)
        
        return jsonify({
            'bmi': round(bmi, 2),
            'suggestions': suggestions
        }), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
