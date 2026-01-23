# How to Run the Glaucoma Detection Project

## Quick Start Guide

### Option 1: Use the Batch Files (Easiest)

1. **Double-click `start-all.bat`** - This will start both services in separate windows
   - Backend API: http://localhost:8236
   - Frontend UI: http://localhost:3000

2. **Or start them separately:**
   - Double-click `start-backend.bat` for the API
   - Double-click `start-frontend.bat` for the UI

### Option 2: Manual Start (Recommended for seeing errors)

#### Step 1: Start the Backend API

1. Open a **Command Prompt** or **PowerShell**
2. Navigate to the project directory:
   ```cmd
   cd glaucoscan-API
   ```
3. Start the API:
   ```cmd
   python app.py
   ```
4. Wait for the message: "Models loaded and API ready to serve requests"
5. The API will be available at: **http://localhost:8236**
6. API Documentation: **http://localhost:8236/docs**

#### Step 2: Start the Frontend UI

1. Open a **NEW** Command Prompt or PowerShell window
2. Navigate to the UI directory:
   ```cmd
   cd glaucoscan-UI
   ```
3. Start the frontend:
   ```cmd
   npm run dev
   ```
4. Wait for the message: "Ready - started server on 0.0.0.0:3000"
5. The UI will be available at: **http://localhost:3000**

## Troubleshooting

### If the links don't open:

1. **Check if services are running:**
   - Open Task Manager (Ctrl+Shift+Esc)
   - Look for `python.exe` and `node.exe` processes

2. **Check if ports are in use:**
   ```cmd
   netstat -ano | findstr ":8236"
   netstat -ano | findstr ":3000"
   ```

3. **Check for errors:**
   - Look at the console windows where you started the services
   - Common issues:
     - Missing Python packages: Run `pip install -r glaucoscan-API/requirements.txt`
     - Missing Node modules: Run `npm install` in `glaucoscan-UI` directory
     - Port already in use: Close other applications using ports 8236 or 3000

4. **Test the backend directly:**
   - Open browser and go to: http://localhost:8236/
   - You should see: `{"status": "Glaucoma Detection API is running"}`

5. **Test the frontend:**
   - Open browser and go to: http://localhost:3000/
   - You should see the Glaucoma Detection website

### First Time Setup

If this is your first time running the project:

1. **Install Python dependencies:**
   ```cmd
   cd glaucoscan-API
   pip install -r requirements.txt
   ```

2. **Install Node.js dependencies:**
   ```cmd
   cd glaucoscan-UI
   npm install
   ```

## Important Notes

- The backend takes 30-60 seconds to start (loading ML models)
- Keep both command windows open while using the application
- The frontend connects to the backend automatically at `http://localhost:8236`
- If you change the backend port, update the frontend `.env.local` file

## Access Points

- **Frontend UI**: http://localhost:3000
- **Backend API**: http://localhost:8236
- **API Documentation**: http://localhost:8236/docs
- **API Health Check**: http://localhost:8236/

