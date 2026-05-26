from sqlalchemy import Column, Integer, String, DateTime
from db import Base


class Model(Base):
    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    price = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    stock = Column(
        Integer,
        nullable=False
    )
    category = Column(
        String,
        nullable=False
    )
