from typing import Optional
from uuid import UUID
from pydantic import BaseModel

class SettingsInsert(BaseModel):
    id: UUID
    note: Optional[bool]
    task: Optional[bool]
    reminder: Optional[bool]
    email: Optional[bool]
    push: Optional[bool]