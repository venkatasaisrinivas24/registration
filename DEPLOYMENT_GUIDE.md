# Deployment Guide - Connect Frontend & Backend

## Quick Steps

### 1. Setup MongoDB (First)
1. Go to https://mongodb.com/atlas
2. Create free cluster
3. Create database user
4. Get connection string (looks like: `mongodb+srv://username:password@cluster.mongodb.net/`)
5. Replace `username` and `password` with your actual credentials

### 2. Deploy Backend to Render
1. Go to https://render.com
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"
4. Connect repository: `venkatasaisrinivas24/registration`
5. Configure:
   - Name: `registration-backend` (or any name)
   - Root Directory: `backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add Environment Variable:
   - Key: `MONGO_URI`
   - Value: Your MongoDB connection string from step 1
7. Click "Create Web Service"
8. Wait for deployment (5-10 minutes)
9. **COPY YOUR RENDER URL** (e.g., `https://registration-backend-abc123.onrender.com`)

### 3. Update Frontend with Backend URL
1. Open `frontend/config.js`
2. Change this line:
```javascript
API_URL: 'http://localhost:5000'
```
To:
```javascript
API_URL: 'https://your-actual-render-url.onrender.com'
```
(Replace with the URL you copied from Render)

3. Save the file

### 4. Push Updated Code to GitHub
```bash
git add .
git commit -m "Update API URL with Render backend"
git push origin main
```

### 5. Deploy Frontend to Vercel
1. Go to https://vercel.com
2. Sign up/Login with GitHub
3. Click "Add New" → "Project"
4. Import `venkatasaisrinivas24/registration`
5. Configure:
   - Framework Preset: Other
   - Root Directory: `frontend`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
6. Click "Deploy"
7. Wait for deployment (1-2 minutes)
8. Get your Vercel URL (e.g., `https://registration-xyz.vercel.app`)

### 6. Test Your Application
1. Open your Vercel URL in browser
2. Fill out the registration form
3. Click Submit
4. You should see "Registration submitted successfully!"
5. Check MongoDB Compass to verify data was saved

## Troubleshooting

### Frontend shows "Network error"
- Check if backend URL in `config.js` is correct
- Make sure backend is running on Render
- Check browser console (F12) for errors

### Backend not receiving requests
- Verify MONGO_URI environment variable is set in Render
- Check Render logs for errors
- Make sure CORS is enabled (already configured in app.py)

### Data not saving to MongoDB
- Verify MongoDB connection string is correct
- Check if IP address is whitelisted in MongoDB Atlas (allow 0.0.0.0/0 for all)
- Check Render logs for database connection errors

## Local Testing (Optional)

To test locally before deploying:

1. Start backend:
```bash
cd backend
pip install -r requirements.txt
set MONGO_URI=your_mongodb_connection_string
python app.py
```

2. Update `frontend/config.js`:
```javascript
API_URL: 'http://localhost:5000'
```

3. Start frontend:
```bash
cd frontend
python -m http.server 3000
```

4. Open http://localhost:3000 in browser
