from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
import datetime


class ModerationLog(Base):
    __tablename__ = "moderation_logs"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(String)
    user_id = Column(String)

    raw_body = Column(String)

    decision = Column(String)
    confidence_score = Column(Float)
    reason_code = Column(String)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)