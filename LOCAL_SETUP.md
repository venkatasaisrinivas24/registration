# Local Testing Setup

## Step 1: Start Backend Locally

1. Open a terminal and navigate to the backend folder:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set your MongoDB connection string (replace with your actual MongoDB URI):
```bash
# Windows PowerShell
$env:MONGO_URI="mongodb://localhost:27017/"

# Windows CMD
set MONGO_URI=mongodb://localhost:27017/

# Or use MongoDB Atlas connection string:
$env:MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/registration_db"
```

4. Run the Flask backend:
```bash
python app.py
```

Backend will run on: http://localhost:5000

## Step 2: Update Frontend for Local Testing

Temporarily change the API_URL in `frontend/script.js`:
```javascript
const API_URL = 'http://localhost:5000';
```

## Step 3: Start Frontend Locally

1. Open another terminal and navigate to frontend folder:
```bash
cd frontend
```

2. Start a local server:
```bash
# Using Python
python -m http.server 3000

# Or using Node.js (if installed)
npx http-server -p 3000
```

3. Open browser and go to: http://localhost:3000

## Step 4: Test the Connection

1. Fill out the registration form
2. Click Submit
3. Check the backend terminal for logs
4. Check MongoDB Compass to see if data was saved

## After Local Testing Works

1. Deploy backend to Render
2. Get the Render URL (e.g., https://registration-xyz.onrender.com)
3. Update `frontend/script.js` with the Render URL
4. Push changes to GitHub
5. Deploy frontend to Vercel
