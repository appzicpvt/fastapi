from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class ContactMessage(Base):
    __tablename__ = "contact_messages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(String)
    is_read = Column(Boolean)
    is_respond = Column(Boolean)
