import os

class Config:
    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
