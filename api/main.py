from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import predict
from api.routes import feedback
from api.routes import predictions

app = FastAPI(
    title="ARanya AI",
    description="AI-powered medicinal plant intelligence system",
    version="1.0"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite frontend
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(predict.router, tags=["Prediction"])
app.include_router(feedback.router, tags=["Feedback"])
app.include_router(predictions.router, tags=["History"])


@app.get("/")
def root():
    return {"message": "ARanya AI API running"}


# Health check (important for deployment)
@app.get("/health")
def health():
    return {"status": "ok"}