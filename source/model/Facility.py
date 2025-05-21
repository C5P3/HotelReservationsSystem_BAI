class Facility:
    def __init__(self, facility_id: int, facility_name: str):
        self._facility_id = facility_id
        self._facility_name = facility_name

    @property
    def facility_id(self) -> int:
        return self.facility_id
    
    @property
    def facility_name(self) -> str:
        return self._facility_name
    
        