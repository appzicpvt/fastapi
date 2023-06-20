from pydantic import BaseModel
from typing import Optional


class CreateContactMessage(BaseModel):
    name: str
    email: str
    message: str

    class Config():
        orm_mode = True


class ContactMessage(CreateContactMessage):
    id: int
    is_read: bool
    is_respond: bool

    class Config():
        orm_mode = True


class UpdateContactMessage(BaseModel):
    is_read: bool
    is_respond: bool

    class Config():
        orm_mode = True
