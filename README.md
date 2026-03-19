# Registration Form System

An information gathering registration form with separate frontend and backend deployments.

## Architecture

- **Frontend**: HTML/CSS/JavaScript (deployed on Vercel)
- **Backend**: Flask API (deployed on Render)
- **Database**: MongoDB (accessible via MongoDB Compass)

## Project Structure

```
├── frontend/
│   ├── index.html      # Registration form
│   ├── style.css       # Styling
│   ├── script.js       # Frontend logic
│   └── vercel.json     # Vercel configuration
├── backend/
│   ├── app.py          # Flask application
│   ├── requirements.txt # Python dependencies
│   ├── Procfile        # Render deployment
│   └── render.yaml     # Render configuration
└── README.md
```

## Form Fields

- Full Name
- Email
- Phone Number
- Date of Birth
- Gender
- Address
- City
- State/Province
- ZIP/Postal Code
- Country
- Occupation
- Company/Organization (optional)
- Education Level
- Areas of Interest (optional)
- Additional Comments (optional)
- Newsletter Subscription (checkbox)
- Terms and Conditions Agreement (required checkbox)

## Setup Instructions

### 1. MongoDB Setup

1. Create a MongoDB Atlas account at https://www.mongodb.com/atlas
2. Create a new cluster
3. Create a database user with read/write permissions
4. Get your connection string
5. Connect using MongoDB Compass with the connection string

### 2. Backend Deployment (Render)

1. Push your code to GitHub
2. Go to https://render.com and create an account
3. Create a new Web Service
4. Connect your GitHub repository
5. Set the following:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variable:
   - Key: `MONGO_URI`
   - Value: Your MongoDB connection string
7. Deploy

### 3. Frontend Deployment (Vercel)

1. Go to https://vercel.com and create an account
2. Import your project from GitHub
3. Set root directory to `frontend`
4. Update `script.js` with your Render backend URL
5. Deploy

### 4. Local Development

#### Backend
```bash
cd backend
pip install -r requirements.txt
export MONGO_URI="your_mongodb_connection_string"
python app.py
```

#### Frontend
```bash
cd frontend
# Update API_URL in script.js to http://localhost:5000
# Open index.html in browser or use a local server
python -m http.server 3000
```

## API Endpoints

- `POST /api/register` - Submit registration information
- `GET /api/registrations` - Get all registrations (for admin)
- `GET /api/health` - Health check

## Database Schema

Registrations collection:
```json
{
  "_id": "ObjectId",
  "fullName": "string",
  "email": "string",
  "phone": "string",
  "dateOfBirth": "string",
  "gender": "string",
  "address": "string",
  "city": "string",
  "state": "string",
  "zipCode": "string",
  "country": "string",
  "occupation": "string",
  "company": "string",
  "education": "string",
  "interests": "string",
  "comments": "string",
  "newsletter": "boolean",
  "submittedAt": "datetime",
  "status": "string"
}
```

## Features

- Email validation
- Duplicate email prevention
- Responsive design
- Error handling
- CORS enabled
- MongoDB integration
- Information gathering (no passwords)