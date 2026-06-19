# Persona Adaptive Customer Support Agent

## Overview
An AI-powered customer support system that:
- Detects customer personas
- Retrieves information using RAG
- Generates adaptive responses
- Escalates unresolved issues to human support

## Supported Personas
1. Technical Expert
2. Frustrated User
3. Business Executive

## Tech Stack
- Python
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- OpenAI

## Architecture

User Query
→ Persona Detection
→ Knowledge Retrieval (RAG)
→ Response Generation
→ Escalation Check
→ Human Handoff Summary

## Setup

pip install -r requirements.txt

uvicorn api.main:app --reload

streamlit run frontend/app.py

## Example Queries

Technical:
Can you explain the API authentication failure?

Frustrated:
I tried everything and nothing works!

Executive:
How does this impact business operations?

## Escalation Conditions

- No relevant documents found
- Billing issues
- Legal issues
- Account-sensitive requests

## Future Improvements

- Multi-turn memory
- Sentiment analysis
- Confidence scoring