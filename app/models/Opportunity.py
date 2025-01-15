from sqlalchemy import Column, String, DateTime
from app.modassembly.database.sql.get_sql_session import Base

class Opportunity(Base):
    __tablename__ = 'opportunities'

    Id = Column(String, primary_key=True, nullable=False, unique=True)
    GCLID__c = Column(String, nullable=True)
    CreatedDate = Column(DateTime, nullable=False)
    Admission_Date__c = Column(DateTime, nullable=True)
