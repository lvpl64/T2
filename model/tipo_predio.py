from utils.db import db
from sqlalchemy import Column,Integer,String

class TipoPredio(db.Model):
    __tablename__='tipo_predio'
    id_tipo_predio=Column(Integer, primary_key=True)
    nomre_predio=Column(String(50))

    def __init__(self,nomre_predio):
        self.nomre_predio=nomre_predio