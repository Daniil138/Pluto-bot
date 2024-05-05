from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception

class basket_goods(reference):
    basket_id:int
    good_id:int
    good_count:int
    def __init__(self,
                 basket_id:int =None,
                 good_id:int = None,
                 good_count:int = None):

        super().__init__()
        if good_id != None:
            self.good_id = good_id
        if good_count != None:
            self.good_count = good_count
        if basket_id != None:
            self.basket_id
    @property
    def basket_id(self) ->int:
        return self.__basket_id
    

    @basket_id.setter
    def basket_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__basket_id = value
        
    @property
    def good_id(self) ->int:
        return self.__good_id
    

    @good_id.setter
    def good_id(self,value:int):
        exception_proxy.validate(value,int)
        self.__good_id = value

    @property
    def good_count(self) ->int:
        return self.__good_count
    

    @good_count.setter
    def good_count(self,value:int):
        exception_proxy.validate(value,int)
        self.__good_count = value