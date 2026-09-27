from fastapi  import  FastAPI , Path , HTTPException , Query
import fastapi.responses import JSONResponse
from pydantic import BaseModel, Field ,computred_field
from typing import List, Dict, Annotated, Optional 
import json

app =  FastAPI()

def load_data(): 
    with open ("patients.json", "r") as file:
        data = json.load(file)

    return data

def save_data(data):
    with open("patiens.json","w") as file:
        json.dump(data,file)


class Patient(Basemodel):
    name: Annoate


@app.get("/")
def hello():
    return {"message": "Patient Management System API is running!"}

@app.get("/about")
def about():
    return {"message": "This is a Patient Management System API built with FastAPI."}

@app.get("/view")
def view():
    data = load_data()
    return {"patients": data}


# adding query parameters to filter patients by height, weight or bmi

@app.get("/view/filter")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="sort on the basis of height, weight or bmi"
    ),
    order: str = Query(
        "asc",
        description="order of sorting can be asc or desc"
    )
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Valid orders are: asc, desc"
        )

    data = load_data()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=sort_order
    )

    return sorted_data
# get patient by id
@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve like P001, P002, P003")):
    data = load_data()
    
    if patient_id in data:
        return  data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")