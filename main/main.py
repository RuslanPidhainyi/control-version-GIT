from service import datetime

class main(datetime):
    def __init__(self):
        pass
        
    def display_current_datetime(self):
        dt_service = datetime.DateTimeService()
        current_dt = dt_service.get_current_datetime()
        print(f"Current Date and Time: {current_dt}")

