from pydantic import AnyUrl, BaseModel, EmailStr, computed_field
from typing import Dict, List
class Patient(BaseModel):
    name:str
    email:EmailStr
    linkedin_url: AnyUrl
    age:int
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_detail:Dict[str,str]

    @computed_field
    @property
    def BMI(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
def insert(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print('BMI ',patient.BMI)
    print(patient.allergies)
    print(patient.contact_detail)

    print('Inserted')

patient_info={'name':'Achu','email':'rajputx000@icici.com','linkedin_url':'https://www.linkedin.com/in/ankush-rana-x01/','age':'90','weight':63.0,'height':1.67,'married':0,'allergies':['pollen','dust'],'contact_detail':{'email':'rajputx000@gmail.com','phone':'123456','emergency':'9876543210'}}
patient1=Patient(**patient_info) 
insert(patient1)