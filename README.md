# ChatPDF-RAG

A Retrieval-Augmented Generation (RAG) application built completely from scratch in Python without using LangChain or LlamaIndex.

The project extracts text from PDF documents, converts them into semantic embeddings, retrieves the most relevant information using cosine similarity, and generates grounded answers using Google's Gemini API.

---

## Features

- PDF Text Extraction
- Recursive Text Chunking
- Sentence Transformer Embeddings
- Cosine Similarity Search
- Top-K Retrieval
- Prompt Engineering
- Gemini LLM Integration
- Hallucination Reduction using Retrieval
- Modular Architecture

---

## Tech Stack

- Python
- PyPDF
- Sentence Transformers
- NumPy
- Google Gemini API
- python-dotenv

---

# Architecture

```text
                    +------------------+
                    |   PDF Document   |
                    +------------------+
                              |
                              ▼
                  +----------------------+
                  |   PDF Text Loader    |
                  +----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Recursive Chunking    |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Embedding Generator   |
                 | sentence-transformers |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 |  Vector Store         |
                 | (Embeddings + Chunks) |
                 +-----------------------+
                              ▲
                              │
                    User Question
                              │
                              ▼
                 +-----------------------+
                 | Query Embedding       |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Cosine Similarity     |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Top-K Retriever       |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Prompt Builder        |
                 +-----------------------+
                              |
                              ▼
                 +-----------------------+
                 | Gemini LLM            |
                 +-----------------------+
                              |
                              ▼
                    Grounded Response
```

---

# Project Structure

```
chatpdf-rag/
│
├── chunking/
├── data/
├── embeddings/
├── llm/
├── parser/
├── prompts/
├── retrieval/
├── utils/
├── vectorstore/
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

# Retrieval Pipeline

```
PDF
 │
 ▼
Extract Text
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
Vector Store
 │
 ▼
User Query
 │
 ▼
Query Embedding
 │
 ▼
Cosine Similarity
 │
 ▼
Top-K Chunks
 │
 ▼
Prompt Builder
 │
 ▼
Gemini
 │
 ▼
Answer
```

---

# How it Works

1. Extract text from the PDF.
2. Split the document into overlapping chunks.
3. Convert each chunk into vector embeddings.
4. Convert the user query into an embedding.
5. Compute cosine similarity between the query and document chunks.
6. Retrieve the Top-K most relevant chunks.
7. Construct a prompt containing the retrieved context.
8. Generate a grounded answer using Gemini.

---

# Future Improvements

- FAISS Vector Database
- Hybrid Search (BM25 + Dense Retrieval)
- Cross-Encoder Re-ranking
- Conversational Memory
- Metadata Filtering
- Multi-document Retrieval
- Streaming Responses
- Citation Generation

---

# Learning Outcomes

This project demonstrates understanding of:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Cosine Similarity
- Prompt Engineering
- LLM Integration
- Modular AI System Design
