from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Optional, Dict, Annotated

class patient(BaseModel):
    name: Annotated[str, Field(max_length=20, title="Name of the patient", description="This field is used to store the name of the patient", json_schema_extra={"example": "Ram"})]
    age : int 
    weight : float 
    email : Optional[EmailStr] = None
    married : Optional[bool] = None
    # Note: In Pydantic v2, max_length constraints on lists are applied using Field(max_length=5)
    allergies : List[str] = Field(max_length=5)
    contact_details : Dict[str, str]

    @field_validator('email')  
    @classmethod
    def email_validator(cls, value: Optional[str]):
        if value is None:
            return value
            
        allowed_domains = ["gmail.com", "yahoo.com", "hotmail.com"]
        
        if '@' in value:
            domain_name = value.split('@')[-1]
            if domain_name not in allowed_domains:
                raise ValueError("Invalid email domain. Allowed domains are: @gmail.com, @yahoo.com, @hotmail.com")
        else:
            raise ValueError("Invalid email format")

        return value 

    @field_validator('name') 
    @classmethod
    def name_validator(cls, value: str):
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters")
        return value

def insert_patient_data(patient_data: patient):
    print(patient_data.name)
    print(patient_data.age)
    print(patient_data.weight)
    print(patient_data.married)
    print(patient_data.allergies)
    print(patient_data.contact_details)
    print("successfully inserted patient data")

def update_data(patient_data: patient):
    print(patient_data.name)
    print(patient_data.age)
    print("successfully updated patient data")

pateint_data = patient(
    name="Ram", 
    age=40, 
    weight=34.89,
    email="abc@gmail.com",
    allergies=["pollen", "dust", "1", "2", "3"], 
    contact_details={"Phone": "9876543201", "Adress": "Ktm", "email": "abc@gmail.com"}
)  

object1 = insert_patient_data(pateint_data)
