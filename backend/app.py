from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from datetime import datetime
import re

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['registration_db']
registrations_collection = db['registrations']

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['fullName', 'email', 'phone', 'dateOfBirth', 'gender', 
                          'address', 'city', 'state', 'zipCode', 'country', 
                          'occupation', 'education', 'terms']
        for field in required_fields:
            if field == 'terms':
                if not data.get(field):
                    return jsonify({'message': 'You must agree to the terms and conditions'}), 400
            elif not data.get(field):
                return jsonify({'message': f'{field} is required'}), 400
        
        full_name = data['fullName'].strip()
        email = data['email'].strip().lower()
        phone = data['phone'].strip()
        date_of_birth = data['dateOfBirth']
        gender = data['gender']
        address = data['address'].strip()
        city = data['city'].strip()
        state = data['state'].strip()
        zip_code = data['zipCode'].strip()
        country = data['country'].strip()
        occupation = data['occupation'].strip()
        company = data.get('company', '').strip()
        education = data['education']
        interests = data.get('interests', '').strip()
        comments = data.get('comments', '').strip()
        newsletter = data.get('newsletter', False)
        
        # Validate email format
        if not validate_email(email):
            return jsonify({'message': 'Invalid email format'}), 400
        
        # Check if email already exists
        if registrations_collection.find_one({'email': email}):
            return jsonify({'message': 'Email already registered'}), 409
        
        # Create registration document
        registration_doc = {
            'fullName': full_name,
            'email': email,
            'phone': phone,
            'dateOfBirth': date_of_birth,
            'gender': gender,
            'address': address,
            'city': city,
            'state': state,
            'zipCode': zip_code,
            'country': country,
            'occupation': occupation,
            'company': company,
            'education': education,
            'interests': interests,
            'comments': comments,
            'newsletter': newsletter,
            'submittedAt': datetime.utcnow(),
            'status': 'pending'
        }
        
        # Insert registration into database
        result = registrations_collection.insert_one(registration_doc)
        
        if result.inserted_id:
            return jsonify({
                'message': 'Registration submitted successfully',
                'registrationId': str(result.inserted_id)
            }), 201
        else:
            return jsonify({'message': 'Failed to submit registration'}), 500
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/api/registrations', methods=['GET'])
def get_registrations():
    try:
        registrations = list(registrations_collection.find({}))
        for reg in registrations:
            reg['_id'] = str(reg['_id'])
        return jsonify({'registrations': registrations}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'message': 'Internal server error'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'timestamp': datetime.utcnow()}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)