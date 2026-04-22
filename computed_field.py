from pydantic import BaseModel,EmailStr,AnyUrl, Field, computed_field
from typing import List,Dict,Annotated,Optional

class Patient(BaseModel):

    name : Annotated[str,Field(max_length=50,description="enter the name of patient")]
    email: EmailStr
    linkedin: AnyUrl
    age : int = Field(gt=0,lt=100)
    weight : float = Field(gt=0)
    height : float = Field(gt=0)
    married : Annotated[bool,Field(default=False,description="enter the person is married or not")]
    allergies: Optional[list[str]]
    contact: Dict[str,str]

    # we have to compute the bmi using computd filed.
    # creating a new field based on the existing fields

    @computed_field(return_type=float)
    @property
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)




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
"weight": 55.56,
"height":5.4,
# "married":
"allergies":["agryeu","greugew","vgewh"],
"contact":{"mobile":"3245654898","emergency":"4564531323"}
}

patient_2 = Patient(**patient_info)

#
# print(patient_2)
update_function(patient_2)

