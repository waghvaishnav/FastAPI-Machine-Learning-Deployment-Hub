from pydantic import BaseModel

class Address(BaseModel):

    state: str
    dist : str
    pin : int

class Patient(BaseModel):

    name : str = "vaishnav"
    age : int
    address : Address


# def update_function(patient :Patient ):
#
#     print(patient.address.state)
#     print(patient.address.dist)
#     print(patient.address.pin)
#     print(patient.address)
#     print("all patients updated succesfully.")


add_dict = {"state":"maharashtra","dist":"ahilyanagar","pin":454601}
add_obj = Address(**add_dict)

patient_dict = {"age":26,"address":add_obj}
pant_obj = Patient(**patient_dict)

# update_function(pant_obj)

# serialization is the process in which converts the modle into dictionary or json format

# 1.model_dump (dict format)
temp = pant_obj.model_dump()
print(temp)
print(type(temp))

# 2.model_dump_json  (str format)
temp = pant_obj.model_dump_json()
print(temp)
print(type(temp))


# a. include = {}
temp = pant_obj.model_dump(include={
        "name": True,
        "age": True,
        "address": {"state"}})
print(temp)
print(type(temp))

# b. exlude unset = true/false (it removes the predefined fields or saves only fields present in the object.)
temp = pant_obj.model_dump(exclude_unset=True)
print(temp)
print(type(temp))


# c. exclude = {}
temp = pant_obj.model_dump(exclude={
        "name": True,
        "age": True,
        "address": {"state"}})
print(temp)
print(type(temp))

# exclude / inlcude = {"fewf":["fhre"]}  include or exclude inside the particular dictionary field.