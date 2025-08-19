from fastapi import FastAPI, HTTPException
from typing import List
from models import Employee
from db import employee_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/employees", response_model=List[Employee])
def get_employees():
    if not employee_db:
        raise HTTPException(status_code=404, detail="No employees found")
    return employee_db

@app.get("/employee/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    for employee in employee_db:
        if employee["id"] == employee_id:
            return Employee(**employee)
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employee", response_model=Employee)
def create_employee(new_employee: Employee):
    for emp in employee_db:
        if emp["id"] == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employee_db.append(new_employee.model_dump())
    return new_employee

@app.put("/employee/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: Employee):
    for idx, emp in enumerate(employee_db):
        if emp["id"] == employee_id:
            employee_db[idx] = employee.model_dump()
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employee/{employee_id}", response_model=dict)
def delete_employee(employee_id: int):
    for idx, emp in enumerate(employee_db):
        if emp["id"] == employee_id:
            del employee_db[idx]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")