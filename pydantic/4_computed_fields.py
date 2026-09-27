from pydantic import BaseModel, EmailStr, computed_field, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name: Annotated[str, Field(max_length=20, title="Name of the patient", description="This field is used to store the name of the patient", json_schema_extra={"example": "Ram"})]
    age : int 
    weight : float 
    height : float
    married : Optional[bool] = None
    allergies : List[str] = Field(max_length=5)
    contact_details : Dict[str, str]

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

    #  Added decorators so it behaves as an serialization field parameter property
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)


def insert_patient_data(patient_data: patient):
    print(patient_data.name)
    print(patient_data.age)
    print(patient_data.weight)
    print(patient_data.married)
    print(patient_data.height)
    print("adult",patient_data.is_adult)
    print("Bmi", patient_data.bmi)
    print(patient_data.allergies)
    print(patient_data.contact_details)
    print("successfully inserted patient data")

pateint_data = patient(
    name="Ram", 
    age=40, 
    weight=34.89,
    height=1.75,
    allergies=["pollen", "dust", "1", "2", "3"], 
    contact_details={"Phone": "9876543201", "Adress": "Ktm", "email": "abc@gmail.com"}
)  

object1 = insert_patient_data(pateint_data)



