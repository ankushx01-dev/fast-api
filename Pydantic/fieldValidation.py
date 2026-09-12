from pydantic import AnyUrl, BaseModel, EmailStr, field_validator
from typing import Dict, List
class Patient(BaseModel):
    name:str
    email:EmailStr
    linkedin_url: AnyUrl
    age:int
    weight:float
    married:bool=False
    allergies:List[str]
    contact_detail:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]#@gmail.com
        if domain_name not in valid_domain:
            raise ValueError('Not a valid Domain')
        return value
    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError('Enter Valid Age')

def insert(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_detail)

    print('Inserted')

patient_info={'name':'Achu','email':'rajputx000@icici.com','linkedin_url':'https://www.linkedin.com/in/ankush-rana-x01/','age':20,'weight':63.0,'married':0,'allergies':['pollen','dust'],'contact_detail':{'email':'rajputx000@gmail.com','phone':'123456'}}
patient1=Patient(**patient_info) 
insert(patient1)