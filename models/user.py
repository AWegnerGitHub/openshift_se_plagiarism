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
    employee = Column(Boolean, nullable=False, default=False)
    creation_date = Column(DateTime, nullable=False)
    registration_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    id_site = Column(BigInteger)
    website = Column(models.CoerceUTF8(500, convert_unicode=True), nullable=False)
    profile_link = Column(models.CoerceUTF8(500, convert_unicode=True), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    token_expires = Column(DateTime, nullable=False)
    access_token = Column(models.CoerceUTF8(100, convert_unicode=True), nullable=False)
    access_key = Column(models.CoerceUTF8(100, convert_unicode=True), nullable=False)
    is_admin = Column(Boolean, default=False)
    
    def __init__(self, id, name, employee, creation_date, id_site, website, profile_link,
        access_key, access_token, token_expires):
        self.id = id
        self.name = name
        self.employee = employee
        self.creation_date = creation_date
        self.id_site = id_site
        self.website = website
        self.profile_link = profile_link
        self.access_key = access_key
        self.access_token = access_token
        self.token_expires = datetime.datetime.fromtimestamp(int(token_expires))
    
    def api_filter_string(self):
        """Returns the API filter string that has all the data this model requires"""
        return "!T8i)z4pbvpo_6AX*W-"
    
    def get_id(self):
        return unicode(self.id)
        
    def is_active(self):
        return self.active
        
    def is_anonymous(self):
        """We don't allow anonymous users"""
        return False
        
    def is_authenticated(self):
        """User is authenticated only if token is not expired and is active"""
        if datetime.datetime.utcnow() < self.token_expires and self.active:
            return True
        else:
            return False
        
    def __repr__(self):
        return '<User: id={} (name={}, website={})'.format(self.id, self.name, self.profile_link)