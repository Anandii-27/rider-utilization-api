from fastapi import FastAPI
import psycopg2
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Rider Utilization API is running"}

@app.get("/utilization")
def get_utilization():

    conn = psycopg2.connect(
        host="YOUR_HOST",
        port="5432",
        database="YOUR_DATABASE",
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD"
    )

    query = """
    WITH rider_status AS (
        SELECT
            cs.delivery_partner_id,
            MAX(
                CASE
                    WHEN os.status_id NOT IN (60,78) THEN 1
                    ELSE 0
                END
            ) AS occupied_flag
        FROM logistics.delivery_partner_current_state cs
        LEFT JOIN logistics.order_shipments os
            ON cs.most_recent_allocated_order_id = os.order_id
            AND cs.delivery_partner_id = os.delivery_partner_id
        WHERE cs.is_online = 1
        GROUP BY cs.delivery_partner_id
    )

    SELECT
        SUM(CASE WHEN occupied_flag = 1 THEN 1 ELSE 0 END) AS busy_riders,
        SUM(CASE WHEN occupied_flag = 0 THEN 1 ELSE 0 END) AS free_riders,
        COUNT(*) AS total_riders,
        ROUND(
            100.0 * SUM(CASE WHEN occupied_flag = 1 THEN 1 ELSE 0 END)
            / NULLIF(COUNT(*), 0),
            2
        ) AS utilization_percentage
    FROM rider_status;
    """

    try:
        result = pd.read_sql(query, conn)
        return result.to_dict(orient="records")[0]
    finally:
        conn.close()