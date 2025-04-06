#ATTENDANCE ORM + DB Logic
from models.database import Base
import sqlalchemy as sa 
import sqlalchemy.orm as orm
from models.employee_model import Employee
import datetime



class Attendance(Base):
    __tablename__ = 'attendance'
    id = sa.Column(sa.Integer, primary_key=True ,autoincrement=True)
    employee_id = sa.Column(sa.Integer, sa.ForeignKey('employees.id'), nullable=False)
    date = sa.Column(sa.Date, nullable=False)
    status = sa.Column(sa.String, nullable=False)  
    check_in_time = sa.Column(sa.DateTime, nullable=False)
    check_out_time = sa.Column(sa.DateTime, nullable=True)
    
    employee = orm.relationship("Employee", back_populates="attendances")
    

def add_check_in(session, employee_id, date, check_in_time , status):
    attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id, Attendance.date == date).first()
    #check if the employee already checked in today
    if attendance.status == 'On Time' or attendance.status == 'Late':
        raise ValueError("Employee has already checked in today.")
    #check if the employee is on leave today   
    if attendance.status == 'Leave':
        raise ValueError("Employee is on leave today.")
    #check if the employee is absent today
    if attendance.status == 'Absent':
        raise ValueError("Employee is absent today.")
    
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    shift_start_time = datetime.datetime.combine(date, employee.shift_start_time)
    
    #calculate check_in is late or not 
    if check_in_time > shift_start_time:
            late_duration = calculate_late(check_in_time,shift_start_time)
            status = 'Late'
    else:
        status = 'On Time'
     
    attendance.check_in_time = check_in_time
    attendance.status = status
    session.add(attendance)
    session.commit()
    return late_duration
    
    
def add_check_out(session, employee_id, date, check_out_time ,status):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    attendance = session.query(Attendance).filter(Attendance.employee_id == employee_id, Attendance.date == date).first()
    check_in_time = attendance.check_in_time
    shift_end_time = datetime.datetime.combine(date, employee.shift_end_time)
    
    if check_out_time < shift_end_time:
            early_duration = calculate_early_leaving(session, employee_id, date)
            status = 'Early Leaving'
            
    elif check_out_time > shift_end_time:
            overtime_duration = calculate_overtime(check_out_time,check_in_time)
            status = 'Overtime'
    else:
            status = 'Leave'      
    attendance.check_out_time = check_out_time
    attendance.status = status
    session.add(attendance)
    session.commit()
    return early_duration , overtime_duration


def calculate_late(late_threshold,check_in_time):
            late_duration = (check_in_time - late_threshold).total_seconds()/60*60
            return late_duration


def calculate_early_leaving(check_out_time, shift_end_time): 
            early_duration = (shift_end_time -check_out_time).total_seconds()/60*60
            return early_duration
    
def calculate_overtime(check_in_time,check_out_time):
    if check_in_time and check_out_time:
        normal_hours = 8 *60 *60 
        worked_hours = (check_out_time - check_in_time).total_seconds()/60*60
        if worked_hours > normal_hours:
                overtime_duration = (worked_hours - normal_hours)/60*60
    return overtime_duration
