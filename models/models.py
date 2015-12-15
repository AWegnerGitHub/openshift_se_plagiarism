from sqlalchemy import Column, ForeignKey, Integer, BigInteger, Enum, Boolean, DateTime, Float
from sqlalchemy.types import TypeDecorator, Unicode
from sqlalchemy.orm import relationship, backref

import datetime

class CoerceUTF8(TypeDecorator):
    """Safely coerce Python bytestrings to Unicode
    before passing off to the database."""

    impl = Unicode

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value
        
class User(db.Model):
    """
    The user definition
    """
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(CoerceUTF8(100, convert_unicode=True), nullable=False)
    