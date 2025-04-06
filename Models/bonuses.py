import sqlalchemy as sa 
import sqlalchemy.orm as orm
from models.database import Base
from models.employee_model import Employee


class Bonuses(Base):
    __tablename__ = 'Bonuses'
    id=sa.Column(sa.Integer,primary_key=True , autoincrement=True,unique=True)
    employee_id = sa.Column(sa.Integer , sa.ForeignKey('employees.id'),nullable=False)
    bonus = sa.Column(sa.Integer , nullable=False)
    date = sa.Column(sa.DateTime , nullable=False)
    employee = orm.relationship("Employee", back_populates="Bonuses")
    
def calc_bonus(session,employee_id,over_time):
    min_overtime = 0.5
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if over_time >= min_overtime:
        total_bonus = over_time* employee.salary 
    return total_bonus 
    
def add_bonus(session , employee_id , bonus):
    employee = session.query(Bonuses).filter(employee_id=employee_id).first()
    employee.bonus = bonus
    session.add(employee)
    session.commit() 
        