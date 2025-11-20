# Final Year Project — Setup Guide

This guide explains how to run both the **backend (FastAPI)** and **frontend (React)** for your project. All commands and screenshots are included below.

---

# 🟦 Backend Setup (FastAPI)

### **1. Unzip the project**

```bash
unzip skin-web-app.zip
cd final_year_project
```

### **2. Create virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**

```bash
pip install --upgrade pip
pip install -r app/requirements.txt
```

### **4. Start MySQL locally**

You can use Docker or XAMPP/MAMP/WAMP.

#### **Start MySQL using Docker:**

Install Docker:

* Windows: docs.docker.com/desktop/setup/install/windows-install/
* Mac: docs.docker.com/desktop/setup/install/mac-install/

```bash
docker run --name skindb -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=skindb -p 3306:3306 -d mysql:8
```

### **5. Set environment variables**

```bash
export DB_HOST=localhost
export DB_USER=root
export DB_PASS=password
export DB_NAME=skindb
export UPLOAD_DIR=uploads
```

### **6. Start backend server**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 👉 **Backend running at:**

[http://localhost:8000](http://localhost:8000)

---

# 🟩 Frontend Setup (React)

Open a new terminal.

### **1. Go to frontend folder**

```bash
cd final_year_project
```

### **2. Install dependencies**

```bash
npm install
```

### **3. Run React app**

```bash
npm run dev
```

### 👉 **Frontend running at:**

[http://localhost:5173](http://localhost:5173)

---

# 🎉 Prototype Working Flow

### 1. Open frontend:

👉 [http://localhost:5173](http://localhost:5173)

### 2. Project usage steps:

* Upload multiple face images
* Click **Analyze Skin**
* FastAPI will:

  * Save images to `/backend/uploads/`
  * Run dummy ML / model
  * Predict conditions
  * Suggest products
* UI shows results and images

---

# 📌 How to Start Frontend Again

```bash
cd final_year_project
npm run dev
```

Access frontend:
[http://localhost:5173](http://localhost:5173)

### Screenshot:

![alt text](Screenshot%202025-11-19%20at%2011.44.17%E2%80%AFPM.png)

---

# 📌 How to Start Backend Again

```bash
cd final_year_project/app
source venv/bin/activate
cd ..
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Access Swagger API Docs:

[http://localhost:8000/docs](http://localhost:8000/docs)

### Screenshot:

![alt text](Screenshot%202025-11-19%20at%2011.44.09%E2%80%AFPM.png)

---

# 📁 Project Data

(Add any dataset information here.)
this is our project