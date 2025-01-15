from sqlalchemy import Column, String, DateTime
from app.modassembly.database.sql.get_sql_session import Base

class Opportunity(Base):
    __tablename__ = 'opportunities'

    Id = Column(String, primary_key=True, nullable=False, unique=True, doc="The unique identifier for the Salesforce Opportunity.")
    GCLID__c = Column(String, nullable=True, doc="The Google Click Identifier associated with the Opportunity.")
    CreatedDate = Column(DateTime, nullable=False, doc="The date and time when the Opportunity was created.")
    Admission_Date__c = Column(DateTime, nullable=True, doc="The date of admission associated with the Opportunity.")
