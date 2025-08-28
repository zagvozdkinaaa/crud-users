from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from typing import List
from app.database import engine
from app import models

app=FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/users/', response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email ==  user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail='User already exists')
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users/', response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = users=db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=404, detail='Users not found')
    return users


@app.get('/users/{id}', response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = users=db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@app.put('/users/{id}', response_model=schemas.UserResponse)
def update_user(updated_user: schemas.UserCreate, user_id: int, db: Session = Depends(get_db)):
    user = users=db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    user.email = updated_user.email
    user.username = updated_user.username

    db.commit()
    db.refresh(user)
    return user
    

@app.delete('/users/{id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = users=db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    db.delete(user)
    db.commit()