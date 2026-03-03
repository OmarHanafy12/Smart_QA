# 🚀 Smart_QA

A RAG-based Question Answering system built with LangChain.  
Provide a document, process it, and ask questions about its content.

---

## 📌 Requirements

- Python 3.10+
- pip

---

## ⚙️ Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/OmarHanafy12/Smart_QA.git
cd Smart_QA
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` file

Create a `.env` file in the project root and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

> ⚠️ Do NOT push your `.env` file to GitHub.

### 4️⃣ Run the project

```bash
python app.py
```

---

## 📂 Project Structure

- `app.py` → Main application entry point  
- `retriever.py` → Document retrieval logic  
- `doc_splitter.py` → Document chunking logic  
- `requirements.txt` → Project dependencies  

---

## 🧠 How It Works

1. Load document  
2. Split into chunks  
3. Generate embeddings  
4. Retrieve relevant chunks  
5. Generate answer using the LLM  
