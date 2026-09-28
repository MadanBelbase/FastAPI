from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import List, Dict, Annotated, Optional, Literal
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)

    return data


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)


class Patient(BaseModel):

    id: Annotated[
        str,
        Field(
            ...,
            description="ID of the patient",
            example="P001"
        )
    ]

    name: Annotated[
        str,
        Field(..., description="Name of the patient")
    ]

    city: Annotated[
        str,
        Field(..., description="City where patient lives")
    ]

    age: Annotated[
        int,
        Field(gt=0, description="Age of the patient")
    ]

    gender: Annotated[
        Literal["male", "female", "others"],
        Field(..., description="Gender of the patient")
    ]

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Height of the patient in meters"
        )
    ]

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Weight of the patient in kilograms"
        )
    ]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"

        elif self.bmi < 24.9:
            return "Normal weight"

        elif self.bmi < 29.9:
            return "Overweight"

        else:
            return "Obese"


class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(default=None)
    ]

    city: Annotated[
        Optional[str],
        Field(default=None)
    ]

    age: Annotated[
        Optional[int],
        Field(default=None, gt=0)
    ]

    gender: Annotated[
        Optional[Literal["male", "female", "others"]],
        Field(default=None)
    ]

    height: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]

    weight: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]


@app.get("/")
def hello():

    return {
        "message": "Patient Management System API is running!"
    }


@app.get("/about")
def about():

    return {
        "message": "This is a Patient Management System API built with FastAPI."
    }


@app.get("/view")
def view():

    data = load_data()

    return {"patients": data}


# Adding query parameters to filter patients by height, weight or bmi
@app.get("/view/filter")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight or bmi"
    ),
    order: str = Query(
        "asc",
        description="Order of sorting can be asc or desc"
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


# Get patient by ID
@app.get("/view/{patient_id}")
def view_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient to retrieve like P001, P002, P003"
    )
):

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    else:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )


@app.post("/add")
def add_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient with this ID already exists"
        )

    data[patient.id] = patient.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient added successfully"}
    )


@app.put("/update/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    existing_patient_info = data[patient_id]

    update_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info["id"] = patient_id

    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(
        exclude=["id"]
    )

    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": "Patient updated successfully"}
    )


@app.delete("/delete/{patient_id}")
def delete_patient(
    patient_id: str = Path(
        ...,
        description="The ID of the patient to delete like P001, P002, P003"
    )
):

    data = load_data()

    if patient_id in data:

        del data[patient_id]

        save_data(data)

        return JSONResponse(
            status_code=200,
            content={"message": "Patient deleted successfully"}
        )

    else:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

