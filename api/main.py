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

# Allow all origins (required for Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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