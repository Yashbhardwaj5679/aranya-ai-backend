from fastapi import APIRouter
from database.connection import get_connection

router = APIRouter()

@router.post("/feedback")
def give_feedback(prediction_id: int, reward: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO feedback (prediction_id, reward)
    VALUES (%s,%s)
    """, (prediction_id, reward))

    conn.commit()

    cursor.close()
    conn.close()

    return {"status": "feedback recorded"}