from pydantic import BaseModel
from typing import Dict
class Address(BaseModel):
    city:str
    state:str
    pin:int
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
address_dic={'city':'Kangra','state':'himachal pradesh','pin':176054}
address1=Address(**address_dic)
patient_dic={'name':'achu','gender':'male','age':20,'address':address1}
patient1=Patient(**patient_dic)
print(patient1)
print(patient1.address.pin)