from pydantic import AnyUrl, BaseModel, EmailStr, model_validator
from typing import Dict, List
class Patient(BaseModel):
    name:str
    email:EmailStr
    linkedin_url: AnyUrl
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_detail:Dict[str,str]

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_detail:
            raise ValueError('Patient older than 60must have emg no.')
        return self
def insert(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_detail)

    print('Inserted')

patient_info={'name':'Achu','email':'rajputx000@icici.com','linkedin_url':'https://www.linkedin.com/in/ankush-rana-x01/','age':'90','weight':63.0,'married':0,'allergies':['pollen','dust'],'contact_detail':{'email':'rajputx000@gmail.com','phone':'123456','emergency':'9876543210'}}
patient1=Patient(**patient_info) 
insert(patient1)