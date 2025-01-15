from typing import Any, Dict, List

from sqlalchemy.orm import Session

from app.pipeline.Opportunity import Opportunity


def filter_unsaved_conversions(
    session: Session, records: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    print("filter_unsaved_conversions")
    print(records)
    record_id_set = {record["Id"].__str__() for record in records}
    existing_ids = set(
        str(id_[0])
        for id_ in session.query(Opportunity.Id)
        .filter(Opportunity.Id.in_(record_id_set))
        .all()
    )
    unsaved_records = [
        record for record in records if record["Id"].__str__() not in existing_ids
    ]
    print(unsaved_records)
    return unsaved_records
