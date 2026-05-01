from fastapi import FastAPI
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Content Moderation System")


@app.get("/")
def health_check():
    return {"status": "ok"}