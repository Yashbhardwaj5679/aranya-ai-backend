from fastapi import APIRouter, UploadFile, File
import shutil

from services.mcp.orchestrator import MCPOrchestrator

router = APIRouter()

orchestrator = MCPOrchestrator()


@router.post("/predict")
async def predict_plant(file: UploadFile = File(...)):

    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = orchestrator.run_pipeline("temp.jpg")

    return result