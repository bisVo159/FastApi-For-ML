from fastapi import HTTPException
from sqlalchemy.orm import Session
import models,schemas

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, emp_id: int):
    employee= (db
            .query( models.Employee )
            .filter( models.Employee.id == emp_id)
            .first()
        )
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    return employee

def create_employee(db: Session,employee: schemas.EmployeeCreate):
    existing_employee=(
            db
            .query( models.Employee )
            .filter( models.Employee.email == employee.email)
            .first()
            )
    
    if existing_employee:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_employee=models.Employee(name=employee.name, email=employee.email)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db: Session,emp_id: int,employee: schemas.EmployeeUpdate):
    db_employee=(
            db
            .query( models.Employee )
            .filter( models.Employee.id == emp_id)
            .first()
            )
    
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    if employee.name is not None:
        db_employee.name=employee.name
    
    if employee.email is not None:
        existing=(
                db
                .query( models.Employee )
                .filter( models.Employee.email == employee.email,models.Employee.id != emp_id)
                .first()
                )
        if existing:
            raise HTTPException(status_code=400, detail="Email already in use")

        db_employee.email=employee.email 

    # db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session,emp_id: int):
    db_employee=db.query( models.Employee ).filter( models.Employee.id == emp_id).first()
    
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted successfully"}
    