# 🩺 Symptom-Based Healthcare Chatbot

An intelligent healthcare web application that predicts possible diseases from user symptoms, recommends home remedies, suggests suitable doctors, and supports appointment booking. The project combines **Machine Learning**, **FastAPI**, and **MySQL** to provide quick preliminary healthcare assistance through a user-friendly interface.

---

# 📖 Table of Contents

* Project Overview
* Features
* Tech Stack
* System Architecture
* Project Structure
* Machine Learning Model
* Dataset
* Installation
* Running the Application
* Screenshots
* Future Enhancements
* Author

---

# 📌 Project Overview

The **Symptom-Based Healthcare Chatbot** is designed to help users obtain preliminary health guidance by entering their symptoms. Based on the symptoms provided, the application predicts the most likely disease using a trained Machine Learning model and provides:

* Disease prediction
* Home remedy suggestions
* Doctor recommendations
* Appointment booking support

> **Note:** This application is intended for educational purposes and should not replace professional medical advice.

---

# ✨ Features

* 🤖 AI-powered symptom analysis
* 🩺 Disease prediction using Machine Learning
* 🌿 Home remedy recommendations
* 👨‍⚕️ Doctor recommendation system
* 📅 Appointment booking support
* 🔐 User registration and authentication
* 💾 MySQL database integration
* ⚡ RESTful APIs using FastAPI
* 🎨 Responsive web interface

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Frontend

* HTML5
* CSS3
* JavaScript

## Database

* MySQL

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

# 🏗️ System Architecture

```text
User
   │
   ▼
Frontend (HTML, CSS, JavaScript)
   │
   ▼
FastAPI Backend
   │
   ├── Authentication
   ├── Disease Prediction
   ├── Home Remedies
   ├── Doctor Recommendation
   └── Appointment Booking
   │
   ▼
Machine Learning Model
   │
   ▼
MySQL Database
```

---

# 📂 Project Structure

```text
Symptom-Based-Chatbot/
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── db.py
│   ├── train.jsonl
│   ├── train_shuffled.jsonl
│   └── home_remedies.jsonl
│
├── frontend/
│   ├── index.html
│   ├── doctors.html
│   ├── register/
│   ├── sign-up/
│   └── static/
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🧠 Machine Learning Model

The chatbot uses a supervised Machine Learning model trained on healthcare symptom-disease data.

### Workflow

1. User enters symptoms.
2. Symptoms are preprocessed.
3. The trained model predicts the most probable disease.
4. Home remedies are retrieved.
5. Doctors are recommended.
6. Appointment booking is provided when necessary.

---

# 📊 Dataset

The project uses healthcare datasets containing:

* Disease names
* Symptoms
* Home remedies
* Doctor recommendations

Dataset format:

* JSONL
* Structured symptom-disease mapping

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/anusha-coder21/Symptom-Based-Chatbot.git
```

Move into the project

```bash
cd Symptom-Based-Chatbot
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your `.env` file with your MySQL credentials.

---

# ▶️ Running the Application

Start the FastAPI server

```bash
uvicorn backend.app:app --reload
```

Open your browser and access the frontend.

---

# 📸 Screenshots

## Home Page

![Home](screenshots/home.png)

---

## User Registration

![Register](screenshots/register.png)

---

## Login

![Login](screenshots/login.png)

---

## Chatbot Interface

![Chatbot](screenshots/chatbot.png)

---

## Disease Prediction

![Prediction](screenshots/prediction.png)

---

## Doctor Recommendation

![Doctor](screenshots/doctor.png)

---

# 🚀 Future Enhancements

* Voice-enabled chatbot
* Multiple language support
* AI-based medical report analysis
* Real-time hospital integration
* Location-based doctor search
* Medicine recommendation
* Emergency healthcare assistance

---


