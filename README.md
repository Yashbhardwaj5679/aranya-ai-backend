# ARanya AI
# By Yash Bhardwaj

ARanya AI is a multimodal plant intelligence platform designed to
identify plant species from images and provide verified botanical
knowledge using retrieval-augmented generation.

This repository is structured as a production-style ML system with
clear separation between perception (vision) and reasoning (knowledge).

User Upload Image
        ↓
FastAPI Service
        ↓
MCP Orchestration Layer
        ↓
Feature Engineering Layer
        ↓
ML Prediction Layer (Plant classifier)   ← WE JUST BUILT THIS
        ↓
Contextual Bandit Policy Engine
        ↓
LLM Explanation Generator
        ↓
PostgreSQL Logging
        ↓
Feedback Loop / Policy Update
State 1:-
User
  ↓
POST /predict
  ↓
FastAPI
  ↓
Vision Model
  ↓
Plant Prediction
---------------------------------------------------------------------------
Frontend
    ↓
FastAPI API
    ↓
MCP Orchestrator
    ↓
--------------------------------
| Vision Model (ResNet18)      |
| Environment Model (XGBoost)  |
| Bandit Policy Engine         |
| Strategy Engine              |
| LLM Explanation Generator    |
--------------------------------
    ↓
PostgreSQL Logging
    ↓
Feedback Loop