from pydantic import BaseModel
from datetime import datetime


class ModerationRequest(BaseModel):
    content_id: str
    user_id: str
    timestamp: datetime
    raw_body: str


class ModerationResponse(BaseModel):
    decision: str
    confidence_score: float
    reason_code: str