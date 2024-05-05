from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class basket_model(reference):
    __user_id: int
    def __init__(self,user_id:int = None):
        super().__init__()

        if user_id != None:
            self.user_id = user_id

        

    @property
    def user_id(self) ->int:
        return self.__user_id
    

    @user_id.setter
    def user_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__user_id = value
    
    