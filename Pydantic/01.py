from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the Patient',description='give name less than 50 char',examples=['ankush','achu'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int=Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]#not auto from string to Number
    married:Annotated[bool,Field(default=None)]#default false value 
    allergies:Optional[List[str]]=None#2level validation->list me string hone chahiye
    contact_detail:Dict[str,str]#dic me str hone chahye

def insert(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_detail)

    print('Inserted')

patient_info={'name':'Achu','email':'rajputx000@gmail.com','linkedin_url':'https://www.linkedin.com/in/ankush-rana-x01/','age':20,'weight':63.0,'married':0,'allergies':['pollen','dust'],'contact_detail':{'email':'rajputx000@gmail.com','phone':'123456'}}
patient1=Patient(**patient_info) 

insert(patient1)