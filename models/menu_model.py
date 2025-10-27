from sqlalchemy import Column, Integer, String, Text
from config.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)
