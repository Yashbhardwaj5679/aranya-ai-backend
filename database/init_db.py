from connection import get_connection


def create_tables():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id SERIAL PRIMARY KEY,
                plant VARCHAR(100),
                confidence FLOAT,
                soil VARCHAR(50),
                temperature FLOAT,
                rainfall FLOAT,
                suitability_score FLOAT,
                strategy VARCHAR(100),
                explanation TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id SERIAL PRIMARY KEY,
                prediction_id INTEGER REFERENCES predictions(id) ON DELETE CASCADE,
                reward INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        print("Tables created successfully")

    except Exception as e:
        print(f"Error creating tables: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    create_tables()