from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class activities(reference):
    user_id:int
    orders_count:int
    bot_activities:int
    def __init__(self,user_id:int = None,orders_count:int = None,bot_activities:int = None):
        super().__init__()
        if user_id != None:
            self.user_id = user_id

        if orders_count != None:
            self.orders_count = orders_count
        if bot_activities != None:
            self.bot_activities = bot_activities
    @property
    def user_id(self) ->int:
        return self.__user_id
    

    @user_id.setter
    def user_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__user_id = value

    @property
    def orders_count(self) ->int:
        return self.__orders_count
    

    @orders_count.setter
    def orders_count(self,value:int):
        exception_proxy.validate(value,int)
        self.__orders_count = value

    @property
    def bot_activities(self) ->int:
        return self.__bot_activities
    

    @bot_activities.setter
    def bot_activities(self,value:int):
        exception_proxy.validate(value,int)
        self.__bot_activities = value