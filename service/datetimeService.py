from datetime import datetime

class DateTimeService:
    def get_current_datetime(self) -> datetime:
        return datetime.now()