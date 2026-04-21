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

# checks the bank domain is avilable in email for valid customer
    @field_validator("email")
    @classmethod
    def validation_mail(cls,value):
        valid_domains = ["hdfc.com","icici.com","axis.com"]

        splits_mail = value.split("@")[-1]
        if splits_mail not in valid_domains:
            raise ValueError("not a valid domain email")
        return value

# applies the transformation using the filed  validator on name field

    @field_validator("name")
    @classmethod
    def name_upper(cls,value):
        return value.upper()


# field validator operates in before/after mode in type conversion
    @field_validator("age",mode="after") # when we applies before throws error.
    @classmethod
    def age_validate(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("age should in between 0 to 100 .")


def update_function(patient :Patient ):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("all patients updated succesfully.")



patient_info = {
"name": "ravi",
"email":"waghvaishnav@icici.com",
"linkedin":"https://linkedin.com/in/vaishnav-wagh-8b97a6315",
"age": "45",
"weight": 65,
# "married":
"allergies":["agryeu","greugew","vgewh"],
"contact":{"mobile":"3245654898"}
}

patient_2 = Patient(**patient_info)


print(patient_2)