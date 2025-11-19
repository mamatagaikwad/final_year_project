# final_year_project

✅ OPTION 1 — Run Without Docker (Fastest for local testing)

(Just backend + frontend manually)

🟦 Backend Setup (FastAPI)
1. Unzip the project
unzip skin-web-app.zip
cd final_year_project

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install --upgrade pip
pip install -r app/requirements.txt

4. Start MySQL locally (you can use Docker or XAMPP/MAMP/WAMP)

💡 DATABASE  — start MySQL with Docker:  
install docker on your laptop
windows: https://docs.docker.com/desktop/setup/install/windows-install/
MAC: https://docs.docker.com/desktop/setup/install/mac-install/

docker run --name skindb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=skindb -p 3306:3306 -d mysql:8

5. Set environment variables:

export DB_HOST=localhost
export DB_USER=root
export DB_PASS=password
export DB_NAME=skindb
export UPLOAD_DIR=uploads

6. Start backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload


👉 Backend running at:
http://localhost:8000

🟩 Frontend Setup (React Web)

Open a new terminal:

1. Go to frontend
cd final_year_project

2. Install Node dependencies
npm install

3. Run React app
npm run dev


👉 Frontend runs at:
http://localhost:5173

🎉 Prototype Working Flow

Open frontend
👉 http://localhost:5173


Project usage steps 
    Upload multiple face images
    Click Analyze Skin
    FastAPI will:
    Save images to /backend/uploads/
    Run dummy ML / model
    Predict conditions
    Suggest products
    UI shows results + images



## how to start frontend:
cd final_year_project
npm run dev

Access frontend:
http://localhost:5173

![alt text](<Screenshot 2025-11-19 at 11.44.17 PM.png>)


## how to start backend
cd final_year_project/app
source venv/bin/activate
cd ..
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

How access backend swagger doc:
http://localhost:8000/docs

![alt text](<Screenshot 2025-11-19 at 11.44.09 PM.png>)
## project data
