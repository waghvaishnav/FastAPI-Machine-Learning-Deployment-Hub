from pydantic import BaseModel,EmailStr,AnyUrl, Field, model_validator
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

    # model_validator applied over the all fields insted of single field like field_validator

    @model_validator(mode="after")
    def age_emergency_contacts(cls,model):
        if model.age > 60 and "emergency" not in model.contact:
            raise ValueError("emergency contact is required in contacts for age greater than 60.")
        return model
#
def update_function(patient :Patient ):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("all patients updated succesfully.")



patient_info = {
"name": "ravi",
"email":"waghvaishnav@icici.com",
"linkedin":"https://linkedin.com/in/vaishnav-wagh-8b97a6315",
"age": "65",
"weight": 65,

# "married":
"allergies":["agryeu","greugew","vgewh"],
"contact":{"mobile":"3245654898"}
}

patient_2 = Patient(**patient_info)

#
# print(patient_2)
update_function(patient_2)

