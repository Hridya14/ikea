from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi.middleware.cors import CORSMiddleware

# MySQL Database Connection
DATABASE_URL = "mysql+pymysql://root:hridya2006@localhost/zerowaste_connect"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Create FastAPI app
app = FastAPI()

# ==============================
# DATABASE MODEL (SQLAlchemy)
# ==============================
class FoodDB(Base):
    __tablename__ = "food_listings"

    food_id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String(100))
    quantity = Column(String(50))
    location = Column(String(100))
    ingredients = Column(String(200))
    expiry_time = Column(String(50))
    #food_id = Column(Integer)


# Create table (only creates if not exists)
Base.metadata.create_all(bind=engine)


# ==============================
# Pydantic Model (Validation)
# ==============================
class Food(BaseModel):
    food_name: str
    quantity: str
    location: str
    ingredients: str
    expiry_time: str

    class Config:
        orm_mode = True


# ==============================
# CORS
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================
# ADD FOOD API
# ==============================
@app.post("/addfood")
def add_food(food: Food):
    db = SessionLocal()

    new_food = FoodDB(
        food_name=food.food_name,
        quantity=food.quantity,
        location=food.location,
        ingredients=food.ingredients,
        expiry_time=food.expiry_time
    )

    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    db.close()

    return {
        "message": "Food added successfully",
        "id": new_food.food_id
    }


# ==============================
# GET ALL FOOD API
# ==============================
@app.get("/all")
def get_all_food():
    db = SessionLocal()
    foods = db.query(FoodDB).all()
    db.close()
    return foods
