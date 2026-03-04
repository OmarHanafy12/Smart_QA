# Smart_QA — Retrieval-Augmented Question Answering System

A modular **Retrieval-Augmented Generation (RAG)** application built using **LangChain**.  
The system allows users to process a document and ask grounded questions about its content through an interactive web interface.

---

## 📌 Project Overview

This project demonstrates an end-to-end RAG pipeline:

- Document ingestion (PDF)
- Text extraction and chunking
- Embedding generation
- Vector database indexing
- Semantic retrieval
- LLM-based grounded answer generation
- Interactive Gradio interface
- Dockerized deployment


---

## 🏗️ Project Structure

```
Smart_QA/
│
├── app.py                # Main application entrypoint
├── doc_splitter.py       # Document chunking logic
├── retriever.py          # Retrieval & QA logic
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker configuration
├── chroma_db/            # Auto-generated vector database
├── test_data/            # Sample PDF for testing
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key
```

> Do not commit `.env` to version control.

---

# 🐍 Running Locally (Without Docker)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/OmarHanafy12/Smart_QA.git
cd Smart_QA
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

The Gradio interface will start at:

```
http://127.0.0.1:7860
```

---

# 🐳 Running with Docker

Docker allows you to run the project without manually installing dependencies.

---

## 🔨 Build the Docker Image

```bash
docker build -t smart_qa .
```

---

## ▶️ Run the Container

```bash
docker run -p 7860:7860 --env-file .env smart_qa
```

Then open:

```
http://localhost:7860
```
