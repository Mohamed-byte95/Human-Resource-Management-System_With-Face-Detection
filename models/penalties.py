import sqlalchemy as sa 
import sqlalchemy.orm as orm
from  models.database import Base
from models.employee_model import Employee

class Penalty(Base):
    __tablename__='Penalty'
    id =sa.Column(sa.Integer,primary_key=True,autoincrement=True,nullable=False)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.id'),nullable=False)
    penalty  = sa.Column(sa.Float,nullable=True)
    employee = orm.relationship("Employee", back_populates="Penalty")
    
def cal_penalty(session,employee_id,late_time):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    penal_val = late_time * employee.salary 
    return penal_val


    
    