# 🤖 Intent Classification Agent (ADK + Gemini + FastAPI)

A full-stack AI **intent classification agent** built using **Google ADK** and **Gemini (Vertex AI)**.
It provides a simple web interface and API to classify user intent in real time.

---

## 🚀 Features

* 🤖 AI-powered **intent classification agent**
* 🌐 Simple frontend (`index.html`)
* ⚡ FastAPI backend
* 🧠 Powered by Gemini (Vertex AI)
* ☁️ Deployable on Google Cloud Run
* 📦 Dockerized for easy deployment

---

## 📁 Project Structure

```id="2nt9hu"
intent-agent/
├── app/
|      ├── agent.py          # ADK agent definition
|      ├── main.py           # FastAPI backend
|      ├── index.html        # Frontend UI
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🧠 How It Works

```id="9x4r45"
User Input (Browser)
        ↓
Frontend (index.html)
        ↓
FastAPI API (/classify)
        ↓
ADK Agent (intent_classifier_agent)
        ↓
Gemini (Vertex AI)
        ↓
Structured JSON Response
```

---

## ⚙️ Tech Stack

### Frontend

* HTML
* JavaScript (Fetch API)

### Backend

* Python (FastAPI)
* Google ADK (Agent Development Kit)
* Gemini 2.5-flash (Vertex AI)

### Deployment

* Docker
* Google Cloud Run


---


## 🔒 Notes

* Enable required Google Cloud APIs (Cloud Run, Vertex AI, Artifact Registry)
* Update API URL in `index.html` after deployment
* Backend must be running for frontend to work

---

## 📌 Future Improvements

* Authentication (JWT)
* Database integration
* Multi-intent classification


