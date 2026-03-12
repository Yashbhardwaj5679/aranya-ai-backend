from fastapi import APIRouter
from database.connection import get_connection

router = APIRouter()


@router.get("/predictions")
def get_predictions():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, plant, confidence, suitability_score,
               strategy, created_at
        FROM predictions
        ORDER BY created_at DESC
        LIMIT 20
    """)

    rows = cursor.fetchall()

    results = []

    for r in rows:
        results.append({
            "prediction_id": r[0],
            "plant": r[1],
            "confidence": r[2],
            "suitability": r[3],
            "strategy": r[4],
            "timestamp": r[5]
        })

    cursor.close()
    conn.close()

    return results