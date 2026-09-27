from pydantic import BaseModel ,EmailStr , Field 
from typing import List, Optional,Dict,Annotated


class patient(BaseModel):
    name: Annotated[str, Field(max_length=20 , title="Name of the patient",  description="This field is used to store the name of the patient", example="Ram") ]
    age : int 
    weight : float 
    # email : Optional[EmailStr] = None
    married : Optional[bool] = None
    allergies : List[str] = Field(max_length=5)
    contact_details : Dict[str,str]


def insert_patient_data(patient_data: patient):
    # Here you would typically insert the patient data into a database
    # For demonstration purposes, we'll just return the data
    print(patient_data.name)
    print(patient_data.age)
    print(patient_data.weight)
    print(patient_data.married)
    print(patient_data.allergies)
    print(patient_data.contact_details)
    print("successfully inserted patient data")

def update_data(patient_data:patient):
    print(patient_data.name)
    print(patient_data.age)
    print("successfully updated patient data")


#  pateint_data = patient(name="Ram", age= "40" , weights = "34.89",married = True,allergies = ["a","b"],contact_details = {"adree":"address"})
pateint_data = patient(
    name="Ram", 
    age=40, 
    weight=34.89,
    # email = "abc@gmail.com",
    # married=True, 
    allergies=["pollen", "dust","1","2","3"], 
    contact_details={"Phone": "9876543201", "Adress": "Ktm", "email ":"abc@gmail.com"}
)  

print("first operation insert data")
object1 = insert_patient_data(pateint_data)
print("sceond operatiion update data")
object2 = update_data(pateint_data)

