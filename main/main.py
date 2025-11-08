from model import userModel as user
from service import datetimeService as datetime

class main(datetime, user):
    def __init__(self):
        pass
        
    def display_current_datetime(self):
        dt_service = datetime.DateTimeService()
        current_dt = dt_service.get_current_datetime()
        print(f"Current Date and Time: {current_dt}")
    
    def create_user(self, username: str, password: str):
        new_user = user.UserModel(username, password)
        print(f"User '{new_user.username}' created successfully.")

