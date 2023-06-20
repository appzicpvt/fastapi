from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from crud import create_item, read_all_items, read_item, update_item, delete_item
from . import schemas, models

router = APIRouter(
    prefix="/contact-messages",
    tags=["Contact Messages"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CreateContactMessage
)
def create_contact_message(
    contact_message: schemas.CreateContactMessage,
    db: Session = Depends(get_db)
):
    new_contact_message = create_item(
        db=db,
        model=models.ContactMessage,
        values={
            "name": contact_message.name,
            "email": contact_message.email,
            "message": contact_message.message,
            "is_read": False,
            "is_respond": False
        }
    )
    return new_contact_message


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[schemas.ContactMessage]
)
def read_all_contact_messages(
    db: Session = Depends(get_db)
):
    return read_all_items(
        db=db,
        model=models.ContactMessage
    )


@router.get(
    "/{message_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ContactMessage
)
def read_contact_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    return read_item(
        db=db,
        model=models.ContactMessage,
        id=message_id
    )


@router.put(
    "/{message_id}",
    status_code=status.HTTP_200_OK,
    response_model=schemas.ContactMessage
)
def update_contact_message(
    message_id: int,
    contact_message: schemas.UpdateContactMessage,
    db: Session = Depends(get_db)
):
    return update_item(
        db=db,
        model=models.ContactMessage,
        id=message_id,
        values=contact_message.dict()
    )


@router.delete(
    "/{message_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_contact_message(
    message_id: int,
    db: Session = Depends(get_db)
):
    delete_item(
        db=db,
        model=models.ContactMessage,
        id=message_id
    )
