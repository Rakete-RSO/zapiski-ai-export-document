import uuid

from pydantic import BaseModel


class CompletionRequest(BaseModel):
    message: str
    chat_id: uuid.UUID
