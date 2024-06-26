#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table ('place_amenity', Base.metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                primary_key=True,
                                nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True,
                                nullable=False)   
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
    amenities= relationship('Amenity', back_populates='place_amenities', secondary='place_amenity', viewonly=False)

    @property
    def reviews(self):
        from models import storage
        reviews_list = []

        for review in storage.all(Review).values():
            if review.place_id == self.id:
                    reviews_list.append(review)
        return reviews_list
    
    @property
    def amenities(self):
        """
        returns the list of Amenity instances based on the
        attribute amenity_ids that contains all Amenity.id
        linked to the Place
        """
        return self.amenity_ids
    
    @amenities.setter
    def amenities(self, obj=None):
        split_objects = obj.split()
        class_name = split_objects[0][1:-1]
        if class_name == 'Amenity' and obj.id not in self.amenity_ids:
            self.amenity_ids.append(obj.id)

