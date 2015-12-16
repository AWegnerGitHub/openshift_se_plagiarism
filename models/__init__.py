from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import TypeDecorator, Unicode

db = SQLAlchemy()

class CoerceUTF8(TypeDecorator):
    """Safely coerce Python bytestrings to Unicode
    before passing off to the database."""

    impl = Unicode

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            value = value.decode('utf-8')
        return value
        
from user import User
from setting import Setting
from tag import Tag