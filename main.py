import psycopg
from fastapi import FastAPI

from config import settings

# from dotenv import load_dotenv

# load_dotenv()

app = FastAPI()

# Приветствие сервис берёт из окружения.
# Нет переменной GREETING — сервис не стартует.
# greeting = os.environ["GREETING"]

greeting = settings.greeting


@app.get("/")
def read_root():
    return {"message": greeting}


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    # database_url = os.environ["DATABASE_URL"]
    with psycopg.connect(settings.database_url) as conn:
        conn.execute("SELECT 1")
    return {"db": "ok"}