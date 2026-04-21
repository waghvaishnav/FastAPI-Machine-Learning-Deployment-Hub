from pydantic import BaseModel,EmailStr,AnyUrl, Field, field_validator
from typing import List,Dict,Annotated,Optional

class Patient(BaseModel):

    name : Annotated[str,Field(max_length=50,description="enter the name of patient")]
    email: EmailStr
    linkedin: AnyUrl
    age : int = Field(gt=0,lt=100)
    weight : float = Field(gt=0)
    married : Annotated[bool,Field(default=False,description="enter the person is married or not")]
    allergies: Optional[list[str]]
    contact: Dict[str,str]

def insert_patient(patient :Patient ):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)

    print("all patients inserted succesfully.")
#
# def update_function(patient :Patient ):
#
#     print(patient.name)
#     print(patient.age)
#     print(patient.weight)
#     print("all patients updated succesfully.")

@field_validator("email")
@classmethod
def email_validator(cls,value):
    valid_domains = ["hdfc.com","icici.com","axis.com"]

    splits_mail = value.split("@")[-1]
    if splits_mail not in valid_domains:
        raise ValueError("not a valid domain emain")
    return value


patient_info = {
"name": "ravi",
"email":"waghvaishnav@hdfc.com",
"linkedin":"https://linkedin.com/in/vaishnav-wagh-8b97a6315",
"age": 45,
"weight": 65,
# "married":
"allergies":["agryeu","greugew","vgewh"],
"contact":{"mobile":"3245654898"}
}

patient_1 = Patient(**patient_info)

insert_patient(patient_1)

