from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'ktm', 'state': 'bagmati', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'madan', 'gender': 'male', 'age': 21, 'address': address1}

patient1 = Patient(**patient_dict)
print(patient1)

temp = patient1.model_dump()
print(type(temp))