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

print(patient1.address.pin)
temp=patient1.model_dump()
print(temp)
print(type(temp))

temp2=patient1.model_dump_json()
print(temp2)
print(type(temp2))

personal_info=patient1.model_dump(include=['name','age'])#or exclude to terminate thta we dont need
print(personal_info)