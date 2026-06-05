# Rider Utilization API

This FastAPI service calculates rider utilization from PostgreSQL data.

## Endpoint

GET /utilization

## Response

```json
{
  "busy_riders": 1842,
  "free_riders": 589,
  "total_riders": 2431,
  "utilization_percentage": 75.77
}
```

## Requirements

* FastAPI
* Pandas
* psycopg2-binary
* PostgreSQL access

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Notes

* The API calculates rider utilization using data from PostgreSQL.
* Database credentials in `main.py` are placeholders and should be replaced with actual PostgreSQL connection details during deployment.
* The `/utilization` endpoint returns the latest rider utilization metrics whenever it is called.
