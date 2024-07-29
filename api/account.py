import inspect
from requests.exceptions import HTTPError
from api import BaseAPI

class Account(BaseAPI):
    def __init__(self):
        super().__init__()
        self.auth_session()
        self.url = f'{self.url}/my/'
        
    @property
    def logs(self):
        return self.parse(uri=inspect.currentframe().f_code.co_name)
    
    @property
    def characters(self):
        return self.parse(uri=inspect.currentframe().f_code.co_name)
    
class Bank(BaseAPI):
    def __init__(self):
        super().__init__()
        self.auth_session()
        self.url = f'{self.url}/my/bank/'
        
    @property
    def gold(self):
        return self.parse(uri=inspect.currentframe().f_code.co_name)
    
    @property
    def items(self):
        return self.parse(uri=inspect.currentframe().f_code.co_name)

if __name__ == '__main__':
    account = Account()
    print(account.characters)
    
    bank = Bank()
    print(bank.gold)
    print(bank.items)