import uuid
from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class users(reference):
    __address:str
    __phone:int
    __post_index:int
    __user_inviter:uuid
    
    def __init__(self,
                 name:str=None,
                 address:str =None,phone:int = None,
                 post_index:int = None,user_inviter:uuid = None):
        super().__init__(name)
        
        if address != None:
            self.address = address
        if phone != None:
            self.phone = phone
        if post_index != None:
            self.post_index = post_index
        if user_inviter != None:
            self.user_inviter = user_inviter

    @property
    def address(self) ->str:
        return self.__address
    
    
    @address.setter
    def address(self,value:str):
        exception_proxy.validate(value,str)
        self.__address = value

    @property
    def phone(self) ->int:
        return self.__phone
    
    
    @phone.setter
    def phone(self,value:int):
        exception_proxy.validate(value,int)
        self.__phone= value
    
    @property
    def post_index(self) ->int:
        return self.__post_index
    
    
    @post_index.setter
    def post_index(self,value:int):
        exception_proxy.validate(value,int)
        self.__post_index= value

    @property
    def user_inviter(self) -> uuid:
        return self.__user_inviter
    
    
    @user_inviter.setter
    def user_inviter(self,value:uuid):
        exception_proxy.validate(value,str)
        self.__user_inviter = value
