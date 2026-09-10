import json
from fastapi import FastAPI,Path,HTTPException,Query

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data
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

