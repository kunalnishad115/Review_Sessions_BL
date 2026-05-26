from fastapi import FastAPI

from db import Base, SessionLocal, engine
# from db import Model
from sqlalchemy.orm import Session
from model import Product
from db_model import Model
from fastapi import Depends



Base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home_page():
    return {
        'msg':'home page'
    }

@app.get('/products')
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Model).all()
    return products

@app.post('/products/save')
def save_product(product: Product, db: Session = Depends(get_db)):
    new_product = Model(
        id=product.id,
        name=product.name,
        price=product.price,
        description=product.description,
        stock=product.stock,
        category=product.category
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


@app.get('/products/{id}')
def get_by_id(id: int, db:Session = Depends(get_db)):
    product = db.query(Model).filter(Model.id == id).first()
    if not product:
        return {
            'msg': 'Product not found'
        }
    return product



@app.put('/products/update/{id}')
def update_product(id : int , product: Product, db: Session = Depends(get_db)):
    existing_product = db.query(Model).filter(Model.id == id).first()
    if not existing_product:
        return {
            'msg': 'Product not found'
        }
    
    existing_product.id = product.id
    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.description = product.description
    existing_product.stock = product.stock
    existing_product.category = product.category

    db.commit()
    db.refresh(existing_product)
    return existing_product 


@app.delete('/products/delete/{id}')
def del_product(id: int, db: Session = Depends(get_db)):
    existing_product = db.query(Model).filter(Model.id == id).first()
    if not existing_product:
        return {
            'msg': 'Product not found'
        }
    db.delete(existing_product)
    db.commit()
    return {
        'msg': 'Product deleted successfully'
    } 


# Task 6: Filter Products (Query Params) ⭐
# GET /products?category=electronics&price=1000
# ● Filter products using:
# ○ category
# ○ max price (optional)
# ● Example:
# GET /products?category=electronics
# GET /products?price=500
# GET /products?category=clothing&price=1000
# ● Return filtered list
# ● If no match → empty list

@app.get('/products/filter')
def filter_products(category: str = None, price: float = None, db: Session = Depends(get_db)):
    query = db.query(Model)

    if category:
        query = query.filter(Model.category == category)
    
    if price is not None:
        query = query.filter(Model.price <= price)

    products = query.all()
    return products