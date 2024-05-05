from reference import reference
from exceptions import exception_proxy, argument_exception, operation_exception
#ggg
class basket_model(reference):
    __goods_id: list # айдишников на товары

    def __init__(self, name=None,goods_id:list = None):
        super().__init__(name)

        if goods_id != None:
            self.goods_id = goods_id
    
    @property
    def basket(self) ->list:
        return self.__goods_id
    
    
    @basket.setter
    def basket(self,value:list):
        exception_proxy.validate(value,list)
        self.__goods_id = value
class goods_model(reference):
    __name_goods:str
    def __init__(self, name=None,name_goods:str = None):
        super().__init__(name)

        if name_goods != None:
            self.name_goods = name_goods
    
    @property
    def name_goods(self) ->str:
        return self.__name_goods
    
    
    @name_goods.setter
    def goods(self,value:str):
        exception_proxy.validate(value,str)
        self.__name_goods = value
class goods_in_basket_model(reference):
    __id_goods:int
    __id_basket:int
    def __init__(self, name=None,id_goods:int = None,id_basket:int = None):
        super().__init__(name)

        if id_goods != None:
            self.id_goods = id_goods
        if id_basket != None:
            self.__id_basket = id_basket
    @property
    def id_goods(self) ->int:
        return self.__id_goods
    
    
    @id_goods.setter
    def id_goods(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_goods = value
        
    @property
    def id_basket(self) ->int:
        return self.__id_basket
    
    
    @id_basket.setter
    def id_basket(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_basket = value
class order_model(reference):
    __id_goods: int
    __id_user: int
    def __init__(self, name=None,id_goods:int = None,id_user:int = None):
        super().__init__(name)

        if id_goods != None:
            self.name_goods = id_goods
        if id_user != None:
            self.id_user = id_user
    @property
    def id_goods(self) ->int:
        return self.__id_goods
    
    
    @id_goods.setter
    def id_goods(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_goods = value
    @property
    def id_user(self) ->int:
        return self.__id_user
    
    
    @id_user.setter
    def id_user(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_user = value
class user_model(reference):
    __name_user: str
    def __init__(self, name=None,name_goods:str = None,name_user:str = None):
        super().__init__(name)

        if name_goods != None:
            self.name_goods = name_goods
        if name_user != None:
            self.name_user = name_user
    
    @property
    def name_user(self) ->str:
        return self.__name_user
    
    
    @name_user.setter
    def name_user(self,value:str):
        exception_proxy.validate(value,str)
        self.__name_user = value
class activity_model(reference):
    __id_user: int
    __activity: str
    def __init__(self, name=None,activity:str = None,id_user:int = None):
        super().__init__(name)

        if activity != None:
            self.activity = activity
        if id_user != None:
            self.id_user = id_user
    @property
    def activity(self) ->str:
        return self.__activity
    
    
    @activity.setter
    def activity(self,value:str):
        exception_proxy.validate(value,str)
        self.__activity = value
    @property
    def id_user(self) ->int:
        return self.__id_user
    
    
    @id_user.setter
    def id_user(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_user = value
class refer_model(reference):
    __id_user:int
    __count: int
    def __init__(self, name=None,count:int = None,id_user:int = None):
        super().__init__(name)

        if count != None:
            self.count = count
        if id_user != None:
            self.id_user = id_user
    @property
    def count(self) ->int:
        return self.__count
    
    
    @count.setter
    def count(self,value:int):
        exception_proxy.validate(value,int)
        self.__count = value
    @property
    def id_user(self) ->int:
        return self.__id_user
    
    
    @id_user.setter
    def id_user(self,value:int):
        exception_proxy.validate(value,int)
        self.__id_user = value
