from pydantic import BaseModel

class Bar(BaseModel):
    time : str
    open : float
    high : float
    low : float
    close : float
    volume : int


class Strategy(BaseModel):
    position_size:int
    order_action:str
    order_contracts:int
    order_price:float
    order_id:str
    market_position:str
    market_position_size:int
    prev_market_position:str
    prev_market_position_size:int


class MessageAlert(BaseModel):
    passpharase : str
    time : str
    exchange : str
    ticker : str
    bar : Bar
    strategy : Strategy