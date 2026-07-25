# 🤖 ICEBEAR Chat API

A simple AI-powered Chat API built with **FastAPI** and **OpenRouter**. This project demonstrates how to build a clean REST API that accepts user messages, validates input, communicates with an AI model, and returns structured JSON responses.

---

## 🚀 Features

- 💬 AI Chat Endpoint
- ✅ Request Validation with Pydantic
- ⚠️ Custom Error Handling using HTTPException
- 🧠 System Prompt for consistent AI responses
- 🕒 Timestamp included in every response
- 📂 Clean and modular project structure
- 📖 Interactive API documentation with Swagger UI

---

## 📁 Project Structure

```
Day8/
│
├── main.py
├── models.py
├── services.py
├── utils.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- OpenRouter API
- OpenAI Python SDK
- Pydantic
- python-dotenv
- Uvicorn

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/icebear-chat-api.git
```

### 2. Navigate to the project folder

```bash
cd icebear-chat-api
```

### 3. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📮 API Endpoint

### POST `/chat`

#### Request

```json
{
    "message": "Explain FastAPI in simple words."
}
```

#### Success Response

```json
{
    "reply": "FastAPI is a modern Python framework used to build APIs quickly and efficiently.",
    "time": "2026-07-25 21:30:15"
}
```

---

### Invalid Request

```json
{
    "message": ""
}
```

#### Error Response

```json
{
    "detail": "Message cannot be empty."
}
```

---

## 📦 Requirements

```
fastapi
uvicorn
openai
python-dotenv
```

---

## 🎯 Learning Objectives

This project demonstrates:

- Creating REST APIs with FastAPI
- Using Pydantic models for request validation
- Handling errors with HTTPException
- Integrating AI models using OpenRouter
- Organizing FastAPI projects into multiple modules
- Returning structured JSON responses
- Using environment variables securely

---

## 👨‍💻 Author

Built as part of my FastAPI learning journey to understand AI-powered API development.

---

## ⭐ If you found this project helpful

Give this repository a ⭐ on GitHub!