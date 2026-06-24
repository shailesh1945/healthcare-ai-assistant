# Healthcare AI Assistant using RAG, Ollama & FastAPI

## Overview

Healthcare AI Assistant is a Retrieval-Augmented Generation (RAG) based application that answers healthcare-related questions using a predefined healthcare knowledge base.

The system ingests healthcare documents, generates embeddings, stores them in a vector database, retrieves relevant context based on user queries, and generates grounded responses using a local Large Language Model (LLM) powered by Ollama.

This project was developed as part of an AI Engineering Hackathon assignment to demonstrate practical knowledge of:

- Retrieval-Augmented Generation (RAG)
- Local LLM Integration
- Vector Databases
- Prompt Engineering
- Agentic Workflows
- FastAPI Development
- Docker Deployment
- Healthcare AI Safety Considerations

---

# Features

- Document ingestion pipeline
- Healthcare document chunking
- Semantic search using embeddings
- ChromaDB vector storage
- Retrieval-Augmented Generation (RAG)
- Local LLM using Ollama (Mistral)
- Source citations in responses
- Confidence scoring
- Hallucination prevention
- Appointment scheduling tool workflow
- REST API using FastAPI
- Dockerized deployment
- Logging and error handling
- Unit tests

---

# Tech Stack

## Backend

- FastAPI
- Python 3.11

## LLM

- Ollama
- Mistral 7B

## RAG Framework

- LangChain

## Embeddings

- BAAI/bge-small-en-v1.5

## Vector Database

- ChromaDB

## Testing

- Pytest

## Deployment

- Docker
- Docker Compose

---

# System Architecture

```text
                    Healthcare Documents
                             |
                             v

                     Document Ingestion
                             |
                             v

                     Text Chunking
                             |
                             v

                  Embedding Generation
                             |
                             v

                      ChromaDB Store

-------------------------------------------------

User Question
      |
      v

Intent Router
      |
      |----------------------|
      |                      |
      v                      v

Appointment Tool        RAG Pipeline
                             |
                             v

                 Similarity Search (ChromaDB)
                             |
                             v

                   Retrieved Context
                             |
                             v

                     Ollama Mistral
                             |
                             v

              Answer + Sources + Confidence
```

---

# Project Structure

```text
healthcare-ai-assistant/

├── app/
│   ├── api/
│   │   ├── ask.py
│   │   ├── ingest.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── agent.py
│   │   ├── embeddings.py
│   │   ├── ingest.py
│   │   ├── llm.py
│   │   ├── logger.py
│   │   ├── middleware.py
│   │   ├── prompts.py
│   │   ├── rag.py
│   │   ├── startup.py
│   │   ├── tools.py
│   │   ├── vector_store.py
│   │   └── config.py
│   │
│   └── main.py
│
├── data/
│
├── vector_store/
│
├── tests/
│   ├── test_health.py
│   ├── test_ingest.py
│   └── test_ask.py
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Dataset

The application uses synthetic healthcare documents covering:

- Appointment Scheduling Policy
- Medication Refill Policy
- Telehealth Guidelines
- HIPAA Privacy Guidelines
- Insurance Eligibility FAQ
- Patient Discharge Instructions

No real patient information, PHI, or confidential healthcare data is used.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/healthcare-ai-assistant.git

cd healthcare-ai-assistant
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Ollama Setup

Install Ollama:

https://ollama.com/download

Pull Mistral model:

```bash
ollama pull mistral
```

Start Ollama:

```bash
ollama serve
```

Verify installation:

```bash
ollama list
```

Expected Output:

```text
mistral
```

---

# Environment Configuration

Create a `.env` file:

```env
MODEL_NAME=mistral

OLLAMA_BASE_URL=http://localhost:11434

CHROMA_DB_PATH=./vector_store

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

TOP_K=3

RETRIEVAL_THRESHOLD=0.50
```

---

# Running the Application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

# Docker Deployment

```bash
docker-compose up --build
```

Application:

```text
http://localhost:8000
```

---

# API Endpoints

## Health Check

### Request

```http
GET /health
```

### Response

```json
{
  "status": "healthy",
  "model": "mistral",
  "vector_store": "./vector_store"
}
```

---

## Document Ingestion

### Request

```http
POST /ingest
```

### Response

```json
{
  "status": "success",
  "documents_processed": 6,
  "chunks_created": 6
}
```

---

## Ask Question

### Request

```http
POST /ask
```

```json
{
  "question": "Can patients request medication refills through telehealth?"
}
```

### Response

```json
{
  "answer": "Yes, patients may request medication refills through telehealth consultations if the medication has already been prescribed.",
  "sources": [
    {
      "document": "medication_refill_policy.txt",
      "chunk": "Patients may request medication refills through telehealth..."
    }
  ],
  "confidence": "high",
  "route": "rag"
}
```

---

# Agentic Workflow

## Appointment Questions

Example:

```text
Can I book a cardiology appointment?
```

Route:

```text
Appointment Tool
```

Response:

```text
Available Cardiology appointment slots are:
10:00 AM, 02:00 PM, 04:30 PM
```

## Knowledge Questions

Example:

```text
Can patients request medication refills through telehealth?
```

Route:

```text
RAG Pipeline
```

Response generated using retrieved healthcare documents.

---

# Prompt Engineering Strategy

The system prompt enforces:

- Use only retrieved context
- No external knowledge
- No guessing
- No unsafe medical advice
- No diagnosis generation
- Professional healthcare responses
- Explicit fallback response when information is unavailable

Fallback Response:

```text
I could not find this information in the provided documents.
```

---

# Hallucination Prevention

The application uses multiple safeguards:

### 1. Retrieval-Based Grounding

Answers are generated only from retrieved document chunks.

### 2. Prompt Constraints

The LLM is instructed not to use external knowledge.

### 3. Similarity Threshold

Low-confidence retrieval results are rejected before generation.

### 4. Source Citation

Retrieved sources are returned alongside every answer.

---

# Confidence Scoring

| Retrieval Score | Confidence |
|----------------|------------|
| >= 0.80 | High |
| 0.60 - 0.79 | Medium |
| < 0.60 | Low |

---

# Testing

Run unit tests:

```bash
pytest -v
```

---

# Design Decisions

## Why RAG instead of Fine-Tuning?

- Easier knowledge updates
- Lower operational cost
- Source traceability
- Reduced hallucinations

## Why ChromaDB?

- Lightweight
- Persistent storage
- Easy local development
- Fast setup

## Why Ollama + Mistral?

- Local inference
- No API cost
- Better privacy
- Suitable for healthcare use cases

## Why Router-Based Agent?

- Deterministic behavior
- Easier debugging
- More predictable healthcare workflows
- Reduced tool invocation errors

---

# Limitations

- Small synthetic dataset
- Simple keyword-based intent routing
- No authentication
- No user memory
- Single-node deployment
- No production monitoring

---

# Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Authentication & Authorization
- PHI Detection
- Audit Logging
- Multi-user Support
- Conversation Memory
- Pinecone / Weaviate Integration
- Kubernetes Deployment
- Advanced Agent Framework
- Healthcare Compliance Enhancements

---

# Author

Developed as part of an AI Engineering Hackathon assignment demonstrating practical implementation of:

- Retrieval-Augmented Generation (RAG)
- LLM Integration
- Vector Databases
- Agentic AI Workflows
- FastAPI Development
- Docker Deployment
