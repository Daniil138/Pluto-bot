from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class orders_model(reference):
    __status: bool
    __basket_id:int
    __user_id:int
    def __init__(self,
                 status:bool = 0,basket_id:int = None,
                 user_id:int = None):
        super().__init__()
        if status != 0:
            self.status = status
        if basket_id != None:
            self.__basket_id = basket_id

        if user_id != None:
            self.user_id = user_id
    
    @property
    def basket_id(self) ->int:
        return self.__basket_id
    

    @basket_id.setter
    def basket_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__basket_id = value

    @property
    def user_id(self) ->int:
        return self.__user_id
    

    @user_id.setter
    def user_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__user_id = value
        
    @property
    def status(self) ->bool:
        return self.__status
    

    @status.setter
    def status(self,value:bool):
        exception_proxy.validate(value,bool)
        self.__status = value
    