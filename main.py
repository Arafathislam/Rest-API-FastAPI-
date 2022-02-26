from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models



app=FastAPI()


class Item(BaseModel):
    id:int
    name:str
    price:int
    description:str
    on_offer:bool

    class Config:
        orm_mode=True



db=SessionLocal()


@app.get('/items',response_model=List[Item],status_code=200)
async def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/items/{items_id}',response_model=Item,status_code=status.HTTP_200_OK)
async def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()

    return item





@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED)
async def create_an_item(item:Item):
    new_item=models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        on_offer=item.on_offer
    )

    db_item=models.query(models.Item).filter(models.item.name==new_item.name).first()
    
    if db_item ==None:
        raise HTTPException(status_code=400,detail="Item already exists")

    db.add(new_item)
    db.commit
    
    return new_item


@app.put('/items/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
async def update_an_item(item_id:id,item:Item):
    item_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_update.name=name
    item_update.price=price
    item_update.descripiton=description
    item_update.on_offer=on_offer

    db.commit()
    return item_update

@app.delete('/items/{item_id}')
async def delete_item(item:int):
    delete_item=db.query(models.Item).filter(models.Item.id==item_id).first()

    if delete_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    db.delete(delete_item)
    db.commit()

    return delete_item


