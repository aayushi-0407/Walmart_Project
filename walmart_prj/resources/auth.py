from flask import Blueprint, request, jsonify, session
from models.users import User, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists'}), 400
    # Set default height and weight (or handle this separately)
  
    user = User(username, password, 0.0, 0.0)
    db.session.add(user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201



@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        session['username'] = username
        return jsonify({'message': 'Logged in successfully'}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@auth_bp.route('/status', methods=['GET'])
def status():
    if 'username' in session:
        return jsonify({'message': f'Logged in as {session["username"]}'}), 200
    return jsonify({'message': 'Not logged in'}), 200

@auth_bp.route('/profile', methods=['POST'])
def create_profile():
    if 'username' not in session:
        return jsonify({'message': 'Not logged in'}), 401

    data = request.get_json()
    height = data.get('height')
    height_unit = data.get('height_unit')
    weight = data.get('weight')
    weight_unit = data.get('weight_unit')

    if height is None or weight is None or height_unit is None or weight_unit is None:
        return jsonify({'message': 'Height, weight, and their units are required'}), 400

    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        return jsonify({'message': 'Height and weight must be numbers'}), 400

    # Convert height to meters
    if height_unit == 'cm':
        height /= 100
    elif height_unit == 'in':
        height *= 0.0254
    elif height_unit != 'm':
        return jsonify({'message': 'Invalid height unit'}), 400

    # Convert weight to kilograms
    if weight_unit == 'lbs':
        weight *= 0.453592
    elif weight_unit != 'kg':
        return jsonify({'message': 'Invalid weight unit'}), 400

    user = User.query.filter_by(username=session['username']).first()
    if user:
        user.height = height
        user.weight = weight
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully'}), 201

    return jsonify({'message': 'User not found'}), 404
