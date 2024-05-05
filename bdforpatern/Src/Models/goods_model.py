from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception
class goods_model(reference):
    __group:str
    __cost:int
    __count:int
    def __init__(self, name:str = None,description:str = None,
                 group:str = None,
                 cost:int = None,count:int = None):
        super().__init__(name)

        if group != None:
            self.group = group
        if cost != None:
            self.cost = cost
        if count != None:
            self.count = count
        if description != None:
            self.description =description
    
    @property
    def group(self) ->str:
        return self.__group
    

    @group.setter
    def group(self,value:str):
        exception_proxy.validate(value,str)
        self.__group = value

    @property
    def cost(self) ->int:
        return self.__cost
    

    @cost.setter
    def cost(self,value:int):
        exception_proxy.validate(value,int)
        self.__cost = value

    @property
    def count(self) ->int:
        return self.__count
    

    @count.setter
    def count(self,value:int):
        exception_proxy.validate(value,int)
        self.__count = value