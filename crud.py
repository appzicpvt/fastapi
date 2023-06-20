from fastapi import HTTPException, status
from sqlalchemy.orm import Session


def create_item(
    db: Session,
    model: any,
    values: dict
):
    """ Create new item

    Parameters
    ------------
        db: Session
            sqlalchemy.orm Session
        model: any
            sqlalchemy orm model
        values: dict
            values as a dict

    Return
    -----------
        Newly created item
    """
    new_item = model(**values)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def read_all_items(
    db: Session,
    model: any
):
    """ Return all items in model

    Parameters
    ------------
        db: Session
            sqlalchemy.orm Session
        model: any
            sqlalchemy orm model

    Return
    -----------
        All items as an array
    """
    items = db.query(model).all()
    return items


def __get_item(
    db: Session,
    model: any,
    id: int
):
    item = db.query(
        model
    ).filter(
        model.id == id
    )
    if item.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="404 NOT FOUND"
        )
    return item


def update_item(
    db: Session,
    model: any,
    id: int,
    values: dict
):
    """ Update an item

    Parameters
    ------------
        db: Session
            sqlalchemy.orm Session
        model: any
            sqlalchemy orm model
        id: int
            Primary key of model 
        values: dict
            values as a dict

    Return
    -----------
        Newly created item
    """
    item = __get_item(db=db, model=model, id=id)
    print(values)
    item.update(values)
    db.commit()
    return item.first()


def read_item(
    db: Session,
    model: any,
    id: int
):
    """ Return specific item using id

    Parameters
    ------------
        db: Session
            sqlalchemy.orm Session
        model: any
            sqlalchemy orm model
        id: int
            Primary key of model 

    Return
    -----------
        Specific item with id
    """
    item = __get_item(
        db=db,
        model=model,
        id=id
    ).first()
    return item


def delete_item(
    db: Session,
    model: any,
    id: int
):
    """ Delete an item using id

    Parameters
    ------------
        db: Session
            sqlalchemy.orm Session
        model: any
            sqlalchemy orm model
        id: int
            Primary key of model
    """
    __get_item(
        db=db,
        model=model,
        id=id
    ).delete(
        synchronize_session=False
    )
    db.commit()
