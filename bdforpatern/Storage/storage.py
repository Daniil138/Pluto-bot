from Src.Models.activities_model import activities
from Src.Models.baskets_goods_model import basket_goods
from Src.Models.baskets_model import basket_model
from Src.Models.goods_model import goods_model
from Src.Models.invited_coins import invited_coins
from Src.Models.orders import orders_model
from Src.Models.users_model import users


class storage():
    data={}

    def __init__(self) -> None:
        pass
        



    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(storage, cls).__new__(cls)

        return cls.instance 
    

    @staticmethod
    def unit_key():
        return "unit_key"
    
    


    