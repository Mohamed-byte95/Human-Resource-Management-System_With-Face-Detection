import sqlalchemy as sa
import sqlalchemy.orm as orm 
from Models.database import Base 
from Models.employee_model import Employee


class Vacations(Base):
    __tablename__= 'vacations'
    vac_id = sa.column(sa.Integer,primary_key=True,autoincrement=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('emplyees.id'),nullable=False)
    vacation = sa.column(sa.Integer,nullable=False)
    date = sa.Column(sa.DateTime,nullable=False)
    status = sa.Column(sa.String,nullable=False)
    employee = orm.relationship("Employee",back_populates="vacations")

#ADD_VACATION  
def add_vacation(session,employee_id,vacation,date):
    employee =  session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        status = "on Vacation"
        new_vacation = Vacations(employee_id=employee_id,vacation=vacation,date=date,status=status)
        session.add(new_vacation)
        session.commit()
    else:
        raise ValueError("Employee not found.") 
    
#get_all_Vacations
def get_all_vacations(session,employee_id):
    vacations = session.query(Vacations).filter(Vacations.employee_id == employee_id).all()
    return vacations

#CHECK VACATION
def check_on_vacation(session,employee_id,date):
    vacation = session.query(Vacations).filter(Vacations.employee_id == employee_id,Vacations.date == date).all()
    if vacation:
        return True
    else:
        return False


def cehck_vacation_limit(session,employee_id):
    vacations = session.query(Vacations).filter(Vacations.employee_id == employee_id).all()
    total_vacations = sum(vacations.vacation for vacation in vacations)
    if total_vacations > 4:
        vac_exced = total_vacations - 4
        return True
    else:
        return False
