#Employee ORM + DB logic
import sqlalchemy as sa
from models.database import Base 

class Employee(Base):
    __tablename__ = 'employees'
    id = sa.Column(sa.Integer, primary_key=True ,autoincrement=True)
    name = sa.Column(sa.String, nullable=False ,unique=True)
    phone= sa.Column(sa.String, nullable=False,unique=True)
    role = sa.Column(sa.String, nullable=False)
    face_id = sa.Column(sa.BLOB, nullable=False)
    salary = sa.Column(sa.Float, nullable=False)
    hire_date = sa.Column(sa.DateTime, nullable=False)
    shift_start_time = sa.Column(sa.Time, nullable=False)
    shift_end_time = sa.Column(sa.Time, nullable=False)
    
def add_employee(session, name,phone ,role, face_id, salary, hire_date ,shift_start_time, shift_end_time):
    # Check if the employee already exists
    if session.query(Employee).filter((Employee.name == name) | (Employee.phone == phone)).first():
        raise ValueError("Employee with this name or phone already exists.")
    else:
        new_employee = Employee(name=name , phone=phone ,role=role, face_id=face_id, salary=salary, hire_date=hire_date, shift_start_time=shift_start_time, shift_end_time=shift_end_time)
    session.add(new_employee)
    session.commit()
    return new_employee

def get_employee(session, employee_id):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    return employee

def get_all_employees(session):
    employees = session.query(Employee).all()
    return employees

def delete_employee(session, employee_id):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        session.delete(employee)
        session.commit()
        return True
    return False

def update_employee(session, employee_id, name=None, phone=None, role=None, face_id=None, salary=None, hire_date=None):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        if name:
            employee.name = name
        if phone:
            employee.phone = phone
        if role:
            employee.role = role
        if face_id:
            employee.face_id = face_id
        if salary:
            employee.salary = salary
        if hire_date:
            employee.hire_date = hire_date
        session.commit()
        return True
    return False
    
 