import sqlalchemy as sa
import sqlalchemy.orm as orm 
from Models.database import Base 
from Models.employee_model import Employee

class Excuses(Base):
    __Tablename__="excuses"
    exc_id = sa.column(sa.Integer,primary_key=True,autoincrement=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('emplyees.id'),nullable=False)
    duration = sa.column(sa.Float,nullable=False,default=0.0)
    reason = sa.Compiled(sa.String,nullable=False)
    date = sa.Column(sa.DateTime,nullable=False)
    status = sa.Column(sa.String,nullable=False)
    on_excuse = sa.Column(sa.Boolean,default=False)
    employee = orm.relationship("Employee",back_populates="excuses")
    
#ADD_EXCUSE   
def add_excuse(session,employee_id,duration,reason,date):
    employee =  session.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        status = "on Excuse"
        new_excuse = Excuses(employee_id=employee_id,duration=duration,reason=reason,date=date,status=status)
        session.add(new_excuse)
        session.commit()
    else:
        raise ValueError("Employee not found.")

#GET_ALL_EXCUSES
def get_all_excuses(session,employee_id):
    excuses = session.query(Excuses).filter(Excuses.employee_id == employee_id).all()
    return excuses
#Check_for_excuse
def check_on_excuse(session,employee_id,date):
    excuses = session.query(Excuses).filter(Excuses.employee_id == employee_id, Excuses.date == date).all()
    if excuses.on_excuse == True:
        return True
    else:
        return False
    
    
    
#CHECK EXCUSES LIMIT
def check_excuse_limit(session,employee_id):
    excuses = session.query(Excuses).filter(Excuses.employee_id == employee_id).all()
    total_duration = sum(excuses.duration for excuse in excuses)
    if total_duration > 4.5:
        return True
    else:
        return False


        