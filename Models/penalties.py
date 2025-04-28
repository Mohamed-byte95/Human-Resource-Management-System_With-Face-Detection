#This model for calculating penalties for employees who are late or absent 
#

import sqlalchemy as sa 
import sqlalchemy.orm as orm
from  Models.database import Base
from Models.employee_model import Employee

class Penalty(Base):
    __tablename__='Penalty'
    id =sa.Column(sa.Integer,primary_key=True,autoincrement=True,nullable=False)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.id'),nullable=False)
    penalty  = sa.Column(sa.Float,nullable=True)
    employee = orm.relationship("Employee", back_populates="Penalty")
    
#ADD_PENALTY
def add_penalty(session,employee_id,penalty):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        new_penalty = Penalty(employee_id=employee_id,penalty=penalty)
        session.add(new_penalty)
        session.commit()
    else:
        raise ValueError("Employee not found.")
    
#GET_ALL_PENALTIES
def get_all_penalties(session,employee_id):
    penalties = session.query(Penalty).filter(Penalty.employee_id == employee_id).all()
    return penalties
    
    
   



    
    