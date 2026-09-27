from pydantic import BaseModel 

class patient(BaseModel):
    name: str
    age : int 

def insert_patient_data(patient_data: patient):
    # Here you would typically insert the patient data into a database
    # For demonstration purposes, we'll just return the data
    print(patient_data.name)
    print(patient_data.age)
    print("successfully inserted patient data")

def update_data(patient_data:patient):
    print(patient_data.name)
    print(patient_data.age)
    print("successfully updated patient data")


pateint_data = patient(name="Ram", age= "40")

object1 = insert_patient_data(pateint_data)

