# APIs allow services and products to communicate,
# without knowing how they do it.
# In this .py file we make a simple API.
from typing import Optional

import uvicorn

# from alpaca_trade_api.rest import REST, TimeFrame
from fastapi import FastAPI

app = FastAPI()
# api = REST()


@app.get("/")  # specifying URL
async def read_root():
    """
    Calling async before def allows code to do
    other stuff while it waits for results from
    an 'other' api
    """
    # results = await api.get_bars(
    #    "TQQQ",
    #    TimeFrame.Hour,
    #    "2021-07-20",
    #    "2021-07-20",
    #    limit=10,
    #    adjustment="raw",
    # ).df
    return {"message": "Hello World."}  # , results


@app.get("/portfolio/{ticker}")
async def read_item(ticker: str, shares: Optional[int] = None):
    return {"ticker": ticker, "shares": shares}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
