from data.config.session import Session
from data.users.userDB import UserDB
from core.database import Database
#from data.config.constants import Constants

class ApplicationContext:
    def __init__(self):
        self.session = Session()
        self.database = Database()
        #self.constants = Constants()
        self.userdb = UserDB(self)
    
    
        