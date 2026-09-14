from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
import json
app=FastAPI()
class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the Patient",example=['POO1'])]
    name:Annotated[str,Field(...,description="Name of the Patient")]
    city:Annotated[str,Field(...,description="city of the patirnt where he lives")]
    age:Annotated[int,Field(..., gt=0,lt=120,description='Age of Patient')]
    gender:Annotated[Literal['male','female','other'],Field(...,description="Gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="height of the pateint in meters")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of the patient in kg")]
    @computed_field
    @property
    def bmi(self)-> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi <30:
            return 'Normal'
        else:
            return "Obese"



def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.get("/")
def hello():
    return {'message':'Patient Management System API'}
@app.get('/about')
def about():
    return {'message':'A Fully functional API to manage your patient records'}
@app.get('/view')
def view():
    data =load_data()
    return data

# path
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str=Path(...,description='ID of the patient in the DB',examples="P0010")):
    #loading patient
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='Patient not found')
    

#query
@app.get('/sort')
def sort_patient(sort_by:str=Query(...,description='Sort on the Bases of weight,height,bmi'),order:str=Query('asc',description='sort in asc or des order')):
    valid_fields=['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invlaid field select form {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order select b/w asc or descending')
    data =load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):
    #load existing data
    data=load_data()

    # check if  patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400,detail='patient Already exists')
    #new patient
    data[patient.id]=patient.model_dump(exclude=['id'])
#save again in json
    save_data(data)
    return JSONResponse(status_code=201,content={'message':'Patient created successfully'})
    
