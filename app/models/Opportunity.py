from sqlalchemy import Column, String, DateTime
from app.modassembly.database.sql.get_sql_session import Base

class Opportunity(Base):
    __tablename__ = 'opportunities'

    type = Column(String, nullable=False, comment="The type of the Salesforce object, e.g., 'Opportunity'.")
    url = Column(String, nullable=False, comment="The URL to access the Salesforce Opportunity object.")
    Id = Column(String, primary_key=True, comment="The unique identifier for the Salesforce Opportunity.")
    GCLID = Column(String, nullable=True, comment="The Google Click Identifier associated with the Opportunity.")
    CreatedDate = Column(DateTime, nullable=False, comment="The date and time when the Opportunity was created.")
    Admission_Date = Column(DateTime, nullable=True, comment="The date of admission associated with the Opportunity.")
