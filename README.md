# PDFQuery
# 📄 Chat with Your PDF — LangChain + AstraDB + Streamlit

A simple yet powerful **ChatPDF-style web app** where you can upload any PDF and ask questions about its content. The app uses **LangChain**, **OpenAI embeddings**, and **AstraDB (Cassandra)** to perform semantic search and generate accurate answers.

---

## 🚀 Features

* 📤 Upload any PDF file
* ✂️ Automatic text extraction & chunking
* 🔍 Semantic search using vector embeddings
* 🤖 AI-powered question answering
* ⚡ Fast and interactive Streamlit UI
* 🔐 Secure API handling using environment variables

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend / AI:** LangChain
* **LLM:** OpenAI (via `langchain-openai`)
* **Vector Database:** AstraDB (via `cassio`)
* **PDF Parsing:** PyPDF2

---

## 📁 Project Structure

```
.
├── app.py              # Main Streamlit application
├── requirements.txt   # Dependencies
├── .env               # Environment variables (NOT pushed to GitHub)
└── README.md          # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

---

### 2️⃣ Create virtual environment (Python 3.10 recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file in the root directory:

```
ASTRA_DB_APPLICATION_TOKEN=your_astra_token
ASTRA_DB_ID=your_db_id
OPENAI_API_KEY=your_openai_key
```

⚠️ **Important:** Never commit your `.env` file.

---

### 5️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧩 How It Works

1. Upload a PDF
2. Text is extracted using **PyPDF2**
3. Text is split into chunks using **RecursiveCharacterTextSplitter**
4. Chunks are converted into embeddings via **OpenAI**
5. Stored in **AstraDB vector store**
6. User query → similarity search → relevant chunks
7. LLM generates answer using retrieved context

---

## ⚠️ Known Limitations

* Uses `load_qa_chain` (will be deprecated in future LangChain versions)
* No chat history (stateless Q&A)
* Processes one PDF at a time
* No source citation display

---

## 🔮 Future Improvements

* 💬 Add chat memory (multi-turn conversations)
* 📚 Support multiple PDFs
* 📌 Show source references for answers
* ⚡ Stream responses (real-time typing effect)
* 🧠 Upgrade to LangChain LCEL (latest standard)
* 🔒 Add authentication

---

## 🛡️ Security Notes

* API keys are stored in `.env`
* `.env` should be added to `.gitignore`

```
.env
```

---

## 🙌 Acknowledgements

* LangChain
* OpenAI
* DataStax AstraDB
* Streamlit

---

## 📌 Author

Built by **Chirag Goyal**

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to improve it!

---
