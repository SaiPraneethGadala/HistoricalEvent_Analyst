"""
Configuration file for Historical Event Analyst
Gemini + FAISS RAG Project
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# --------------------------------------------------------
# Load Environment Variables
# --------------------------------------------------------

load_dotenv()

# --------------------------------------------------------
# Project Paths
# --------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

VECTORSTORE_DIR = DATA_DIR / "vectorstore"

# --------------------------------------------------------
# Chunking Configuration
# --------------------------------------------------------

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# --------------------------------------------------------
# Retrieval Configuration
# --------------------------------------------------------

TOP_K = 5

# --------------------------------------------------------
# Gemini Models
# --------------------------------------------------------

EMBED_MODEL = "models/gemini-embedding-001"

LLM_MODEL = "gemini-2.5-flash"

# --------------------------------------------------------
# API Key
# --------------------------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file."
    )

# --------------------------------------------------------
# FAISS Files
# --------------------------------------------------------

FAISS_INDEX_FILE = VECTORSTORE_DIR / "faiss.index"

METADATA_FILE = VECTORSTORE_DIR / "metadata.pkl"

# --------------------------------------------------------
# Streamlit
# --------------------------------------------------------

PAGE_TITLE = "Historical Event Analyst"

PAGE_ICON = "📚"

LAYOUT = "wide"

# --------------------------------------------------------
# Embedding
# --------------------------------------------------------

EMBED_BATCH_SIZE = 100

# --------------------------------------------------------
# Logging
# --------------------------------------------------------

LOG_LEVEL = "INFO"