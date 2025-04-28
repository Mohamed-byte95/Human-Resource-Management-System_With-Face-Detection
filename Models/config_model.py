import sqlalchemy as sa 
import sqlalchemy.orm as orm
from Models.database import Base


class SystemConfig(Base): 
    __tablename__ = 'system_config'
    id=sa.Column(sa.Integer,primary_key=True , autoincrement=True,unique=True)
    key = sa.Column(sa.String ,unique=True, nullable=False)
    value = sa.Column(sa.Integer , nullable=False)
    description = sa.Column(sa.String,nullable=True)

def seed_default_configs(session):
    default_configs = {
        "late_window":       ("25", "late window in minutes"),
        "early_leave_window": ("15", "early leave window in minutes"),
        "overtime_window":    ("30", "overtime window in minutes"),
        "absence_penalty":       ("100",   "Penalty for full-day absence"),
        "max_excuse_days_month": ("3",     "Maximum excuse days per month"),
        "normal_working_hours":   ("8",     "Normal working hours per day"),
    }

    for key, (value, desc) in default_configs.items():
        existing = session.query(SystemConfig).filter_by(key=key).first()
        if not existing:
            session.add(SystemConfig(key=key, value=value, description=desc))

    session.commit()

def get_config_value(session, key):
    config = session.query(SystemConfig).filter_by(key=key).first()
    if config:
        return config.value
    else:
        raise ValueError(f"Configuration for {key} not found.")
    

