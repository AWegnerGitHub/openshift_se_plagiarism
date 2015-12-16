from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Enum, Boolean, DateTime, Float
from sqlalchemy.orm import relationship, backref
import models
import datetime

class Setting(models.db.Model):
    """This class defines settings that our application uses"""
    __tablename__ = 'settings'
    name = Column(models.CoerceUTF8(125, convert_unicode=True), primary_key=True, unique=True)
    value = Column(models.CoerceUTF8(500, convert_unicode=True), nullable=False)
    user_manage = Column(Boolean, nullable=False, default=True)
    
    def __repr__(self):
        return "<Setting(name='%s', value='%s')>" % (self.name, self.value)

    @classmethod
    def by_name(cls, session, name):
        return session.query(cls.value).filter(cls.name == name).scalar()

    @classmethod
    def update_value(cls, session, name, value):
        session.query(cls).filter_by(name=name).update({"value":value})
        session.commit()