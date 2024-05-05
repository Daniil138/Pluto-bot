from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class invited_coins(reference):
    id_user:int
    coins:int

    def __init__(self,id_user:int =None,coins:int = None):
        super().__init__()

        if id_user != None:
            self.id_user = id_user
        if coins != None:
            self.coins = coins

    @property
    def id_user(self) ->int:
        return self.__id_user
    

    @id_user.setter
    def id_user(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_user = value

    @property
    def coins(self) ->int:
        return self.__coins
    

    @coins.setter
    def coins(self,value:int):
        exception_proxy.validate(value,int)
        self.__coins = value