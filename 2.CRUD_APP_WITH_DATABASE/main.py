from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import Base, engine
from database import get_db
import schemas,crud
from typing import List,Dict

app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/employees",response_model=List[schemas.EmployeeResponse])
def get_employees(db: Session=Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employee/{emp_id}",response_model=schemas.EmployeeResponse)
def get_employee(emp_id:int,db: Session=Depends(get_db)):
    return crud.get_employee(db,emp_id)

@app.post("/create-employee",response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate,db: Session=Depends(get_db)):
    return crud.create_employee(db,employee)

@app.put("/update-employee/{emp_id}",response_model=schemas.EmployeeResponse)
def update_employee(emp_id:int,employee: schemas.EmployeeUpdate,db: Session=Depends(get_db)):
    return crud.update_employee(db,emp_id,employee)

@app.delete("/delete-employee/{emp_id}",response_model=Dict)
def delete_employee(emp_id: int,db: Session=Depends(get_db)):
    return crud.delete_employee(db,emp_id)