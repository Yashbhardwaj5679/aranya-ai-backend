from database.connection import get_connection


def save_prediction(
    plant,
    confidence,
    soil,
    temperature,
    rainfall,
    suitability,
    strategy,
    explanation
):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO predictions
            (plant, confidence, soil, temperature, rainfall, suitability_score, strategy, explanation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """, (
            plant,
            confidence,
            soil,
            temperature,
            rainfall,
            suitability,
            strategy,
            explanation
        ))

        prediction_id = cursor.fetchone()[0]
        conn.commit()
        return prediction_id

    except Exception as e:
        print(f"Error saving prediction: {e}")
        if conn:
            conn.rollback()
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()