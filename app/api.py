from fastapi import FastAPI,status
from fastapi.responses import JSONResponse

from .models import MessageAlert
from .setting import client,message_passpharase


app = FastAPI()

def create_order(side, size, symbol):
    try:
        order = client.create_market_order(symbol=symbol, side=side , size=size)
    except Exception as e:
        return False,e

    return True,order

app.post("set_order")
def set_order(message:MessageAlert):

    if message.passpharase != message_passpharase:
        return JSONResponse(content="invalid passpharse",status_code=status.HTTP_400_BAD_REQUEST)

    side = message.strategy.get("order_action")
    size = message.strategy.get("position_size")
    ticker = message.get("ticker")
    status_order,order = create_order(side,size,ticker)

    if status_order== False:

        return JSONResponse(content=order,status_code=status.HTTP_400_BAD_REQUEST)

    elif status_order==True:
        
        return JSONResponse(content=order,status_code=status.HTTP_202_ACCEPTED)

