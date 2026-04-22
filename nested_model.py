from pydantic import BaseModel

class Address(BaseModel):

    state: str
    dist : str
    pin : int

class Patient(BaseModel):

    name : str
    age : int
    address : Address


def update_function(patient :Patient ):

    print(patient.address.state)
    print(patient.address.dist)
    print(patient.address.pin)
    print(patient.address)
    print("all patients updated succesfully.")


add_dict = {"state":"maharashtra","dist":"ahilyanagar","pin":454601}
add_obj = Address(**add_dict)

patient_dict = {"name":"rajdeep","age":26,"address":add_obj}
pant_obj = Patient(**patient_dict)

update_function(pant_obj)
