# 📚 Historical Event Analyst
### Retrieval-Augmented Generation (RAG) using Gemini API + FAISS + Streamlit

A production-ready Retrieval-Augmented Generation (RAG) application that answers questions about **World War I** using a custom knowledge base of historical documents.

Instead of relying only on an LLM's knowledge, this project retrieves relevant information from indexed documents and generates accurate, context-aware responses using **Google Gemini**.

---

## 🚀 Features

- 📖 Multi-document Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini 2.5 Flash for answer generation
- 🔍 Gemini Embedding API (`gemini-embedding-001`)
- ⚡ FAISS Vector Database
- ✂️ Intelligent document chunking
- 📚 Source citations for retrieved context
- 💬 Interactive Streamlit Chat Interface
- 🗂 Metadata-based retrieval
- 📄 Works with local `.txt` historical documents
- 🔄 Easy index rebuilding
- 🧪 Modular project structure

---

# 🏗 Project Architecture

```
                        User Question
                              │
                              ▼
                    Gemini Query Embedding
                              │
                              ▼
                      FAISS Vector Search
                              │
                              ▼
                 Top-K Relevant Document Chunks
                              │
                              ▼
                     Gemini 2.5 Flash LLM
                              │
                              ▼
                  Context-Aware Final Answer
                              │
                              ▼
                    Source References
```

---

# 📂 Project Structure

```
Historical-Event-Analyst/
│
├── app.py
├── build_index.py
├── requirements.txt
├── README.md
├── .env
│
├── configs/
│      config.py
│
├── data/
│      raw/
│      processed/
│      vectorstore/
│
├── docs/
│      architecture.png
│
├── src/
│
│    ├── ingestion/
│    │      loader.py
│    │      cleaner.py
│    │
│    ├── processing/
│    │      chunker.py
│    │
│    ├── embedding/
│    │      embedder.py
│    │      vector_store.py
│    │
│    ├── retrieval/
│    │      retriever.py
│    │
│    ├── generation/
│    │      gemini_chain.py
│    │      prompt.py
│    │
│    ├── utils/
│    │      helper.py
│    │
│    └── evaluation/
│           evaluate.py
│
└── tests/
```

---

# ⚙️ Tech Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| LLM | Gemini 2.5 Flash |
| Embeddings | Gemini Embedding API |
| Vector Database | FAISS |
| Framework | Streamlit |
| Chunking | LangChain Text Splitters |
| Environment | Python Dotenv |

---

# 📚 Dataset

The project uses **12 custom World War I chapters** stored as `.txt` files.

Example:

```
data/raw/

chapter1.txt
chapter2.txt
...
chapter12.txt
```

Topics include:

- Europe before World War I
- Alliances
- Nationalism
- Sarajevo Assassination
- July Crisis
- Schlieffen Plan
- Trench Warfare
- Verdun
- Somme
- New Weapons
- America Enters the War
- Russian Revolution

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Historical-Event-Analyst.git

cd Historical-Event-Analyst
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

# 🏗 Build the Vector Database

Before running the application, create embeddings and build the FAISS index.

```bash
python build_index.py
```

Output:

```
data/vectorstore/

faiss.index

metadata.pkl
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- Why did World War I begin?
- Explain the July Crisis.
- What was the Schlieffen Plan?
- Describe the Battle of Verdun.
- Explain trench warfare.
- Why did America enter World War I?
- Who was Gavrilo Princip?
- What caused the Russian Revolution?

---

# 🔄 RAG Pipeline

```
TXT Documents

      │

      ▼

Document Loader

      │

      ▼

Text Cleaner

      │

      ▼

Document Chunker

      │

      ▼

Gemini Embedding API

      │

      ▼

FAISS Vector Store

      │

      ▼

Retriever

      │

      ▼

Gemini 2.5 Flash

      │

      ▼

Final Answer
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📈 Future Improvements

- Hybrid Search (BM25 + FAISS)
- Conversation Memory
- Chat History
- PDF Upload Support
- Multi-document Comparison
- Reranking
- Metadata Filtering
- Evaluation Dashboard
- Docker Support
- Deployment on Streamlit Cloud

---

# 📸 Screenshots

Add screenshots here after deployment.

Example:

```
docs/

home.png

chat.png

retrieval.png
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

3. Commit your changes

4. Push to your branch

5. Create a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sai Praneeth**

AI & Machine Learning Engineer

GitHub: https:https://github.com/SaiPraneethGadala

LinkedIn: https:https://www.linkedin.com/in/sai-praneeth-gadala-362259307/

---

⭐ If you found this project helpful, don't forget to **Star** the repository.
