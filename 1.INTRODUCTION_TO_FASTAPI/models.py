from pydantic import BaseModel, Field, StrictInt
from typing import Optional

class Employee(BaseModel):
    id: int = Field(...,gt=0,title="Employee ID")
    name: str = Field(...,min_length=3,max_digits=30)
    department: str = Field(...,min_length=3,max_digits=30)
    age: Optional[StrictInt] = Field(default=None,gt=21)

