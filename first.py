# creating virtual environment:
# python -m venv myenv
# myenv/Scripts/activated     -- pip install fastapi uvicorn pydantic

from fastapi import FastAPI,Path, HTTPException

import json

app = FastAPI()

def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return "Hello, Welcome to the patient management app"

# about section
@app.get("/about")
def about():
    return "This app provides the end to end report and management system for the patient records."

# shows all patient data
@app.get("/view")
def view():
    data = load_data()

    return data

# viewing the particular patient in the data using patient_id
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(...,title="path params",description="add the patient_id here",example="p001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="patient not found")