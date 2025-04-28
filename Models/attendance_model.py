#ATTENDANCE ORM + DB Logic
from Models.database import Base
import sqlalchemy as sa 
import sqlalchemy.orm as orm
from Models.employee_model import Employee
from Models.excuses_model import check_on_excuse
from Models.excuses_model import Excuses
from Models.vacations_model import check_on_vacation
from datetime import timedelta
from config_model import get_config_value
import enum

#clases for check in and check out status 

class check_in_status_enum(enum.enum):
        on_time = "On Time",
        late= "Late"
        absent = "Absent"
class check_out_status_enum(enum.enum):
        early_leaving = "Early Leaving",
        over_time = "Overtime",
        leave = "Leave"
    

#attendance class 
class Attendance(Base):
    __tablename__ = 'attendance'
    id = sa.Column(sa.Integer, primary_key=True ,autoincrement=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.id'), nullable=False)
    date = sa.Column(sa.Date, nullable=False)
    late_val = sa.Column(sa.Float,nullable=True)
    over_time_val = sa.Column(sa.Float , nullable=True)
    early_leave_val = sa.Column(sa.Float , nullable=True)
    check_in_status = sa.Column(sa.Enum(check_in_status_enum), nullable=False)
    check_out_status = sa.Column(sa.Enum(check_out_status_enum), nullable=True)
    check_in_time = sa.Column(sa.DateTime, nullable=False)
    check_out_time = sa.Column(sa.DateTime, nullable=True)
    recognized = sa.Column(sa.Boolean, default=False)
    employee = orm.relationship("Employee", back_populates="attendances")
    

def add_check_in(session, employee_id, date, check_in_time):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    late_window = get_config_value(session, "late_window")
    shift_start_time =  employee.shift_start_time + timedelta(minutes=late_window)
    attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id, Attendance.date == date).first()
    #if employee already checked in today rasie error
    if attendance is  None:
        attendance = Attendance(employee_id=employee_id, date=date, check_in_time=check_in_time)
        #Check for Vacation 
        if check_on_vacation(session, employee_id, date):
            raise ValueError("Employee is on Vacation today.")
        
        if check_in_time > shift_start_time :
            if check_on_excuse(session, employee_id, date):
                print("Employee has an excuse for being late.")
                excuse = session.query(Excuses).filter(Excuses.employee_id == employee_id,Excuses.date == date).first()
                excuse_duration = excuse.duration
                if check_in_time > shift_start_time + timedelta(minutes=excuse_duration):
                    attendance.status = check_in_status_enum.late
                    #how to calculate late duration after excuse duration
                    
                    raise ValueError("Employee is late.")
                
            else:
                attendance.status = check_in_status_enum.late
                attendance.late_val = calculate_late_duration(shift_start_time,check_in_time,session,employee_id,date)
                raise ValueError("Employee is late.")
                
        else:
            attendance.status = check_in_status_enum.on_time
    
        session.add(attendance)
        session.commit()              
    else:
        #to ensure that employee hasn't checked in-today
        print("Employee has already checked in today.")
       
               
def add_check_out(session, employee_id, date, check_out_time):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id, Attendance.date == date).first()
    early_leave_window = get_config_value(session, "early_leave_window")
    over_time_window = get_config_value(session, "overtime_window")
    shift_end_time = employee.shift_end_time
    #check for early leaving 
    if check_out_time < shift_end_time - timedelta(minutes=early_leave_window):
            if check_on_excuse(session, employee_id, date):
                print("Employee has an excuse for leaving early.")
            
            else:
                attendance.status = check_out_status_enum.early_leaving
                attendance.early_leave_val = calculate_early_leaving(check_out_time, shift_end_time,session)

    #check for overtime                    
    elif check_out_time > shift_end_time + timedelta(minutes=over_time_window):
            attendance.status = check_out_status_enum.over_time
            attendance.over_time_val = calculate_overtime(attendance.check_in_time, check_out_time,over_time_window,session)
    else:
            attendance.status = check_out_status_enum.leave     
    attendance.check_out_time = check_out_time
    session.commit()


#if Employee Exceed 0.5 hour of late it is considered as late 
def calculate_late_duration(shift_start_time,check_in_time,session,employee_id,date):
        Attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id,Attendance.date == date).first()
        late_window = get_config_value(session, "late_window")
        shitf_start = shift_start_time + timedelta(minutes=late_window)
        late_duration = (check_in_time - shitf_start ).total_seconds()/60*6
        return late_duration
        
#def calculate_early_leave_duration
def calculate_early_leaving(check_out_time, shift_end_time,session,employee_id,date):
        Attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id,Attendance.date == date).first()
        early_window = get_config_value(session, "early_leave_window") 
        shift_end_time = shift_end_time - timedelta(minutes=early_window)
        early_duration = (shift_end_time -check_out_time).total_seconds()/60*60
        return early_duration
    
def calculate_overtime(check_in_time,check_out_time,over_time_window,session):
    final_check_out_time = check_out_time + timedelta(minutes=over_time_window)
    normal_hours = get_config_value(session, "normal_working_hours")
    overtime_duration = 0
    if check_in_time and check_out_time:
        worked_hours = (final_check_out_time - check_in_time).total_seconds()/60*60
        overtime_duration = (worked_hours - normal_hours)/60*60
    return overtime_duration

