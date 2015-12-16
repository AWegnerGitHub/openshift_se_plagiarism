from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Enum, Boolean, DateTime, Float
from sqlalchemy.orm import relationship, backref
import models
import datetime

class Tag(models.db.Model):
    """This class defines tags we are checking"""
    __tablename__ = 'tags'
    id = Column(models.CoerceUTF8(125, convert_unicode=True), primary_key=True, unique=True)
    wiki_body = Column(models.CoerceUTF8(65000, convert_unicode=True), nullable=True)
    wiki_excerpt = Column(models.CoerceUTF8(700, convert_unicode=True), nullable=True)
    excerpt_creation = Column(DateTime, nullable=False)
    body_creation = Column(DateTime, nullable=False)
    last_check_date = Column(DateTime, nullable=False)
    
    def __repr__(self):
        return "<Wiki(id='%s', last_check_date='{}')>" % (self.id, self.last_check_date)
        
    