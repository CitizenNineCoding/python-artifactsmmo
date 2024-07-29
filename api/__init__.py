import inspect
import json
import requests
from config import cvars
from requests.exceptions import HTTPError
from typing import Dict, List, Literal, Optional

valid_methods = Literal['GET', 'POST']

class BaseAPI:
    def __init__(self) -> None:
        self.url = cvars['BASE_URL']
        self.init_session()
        
    def init_session(self) -> None:
        self.session = requests.Session()
        self.session.headers.update(cvars['headers'])
        
    def auth_session(self) -> None:
        self.session.headers.update(cvars['auth_header'])
        
    def parse(self, url: Optional[str] = None, uri: Optional[str] = None, attr: Optional[str] = None) -> List[dict] | dict | None:
        url = url or self.url
            
        if uri:
            url = url + uri
        
        try:
            response = self.session.get(url)
            response.raise_for_status()    
            content = response.json()['data']
    
            return content if not attr else content.get(attr)
        except HTTPError as e:
            if e.response.status_code in [404, 498]:
                print(repr(e))            
  
    @property
    def status_data(self):
        return self.parse()
        
    @property
    def characters_online(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)
    
    @property
    def announcements(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)
    
    @property
    def version(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)
    
    @property
    def status(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)
    
    @property
    def last_wipe(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)
    
    @property
    def next_wipe(self):
        return self.parse(attr=inspect.currentframe().f_code.co_name)

if __name__ == '__main__':
    base = BaseAPI()
    print(base.status_data)
    print(base.characters_online)
