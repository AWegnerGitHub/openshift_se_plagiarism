from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Enum, Boolean, DateTime, Float
from sqlalchemy.orm import relationship, backref
import models
import datetime
        
class User(models.db.Model):
    """
    The user definition
    """
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(models.CoerceUTF8(100, convert_unicode=True), nullable=False)
    