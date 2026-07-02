import logging
from binance.client import Client

class BinanceClient:
    def __init__(self, api_key, api_secret):
        # Initializing the Binance Client for Testnet
        self.client = Client(api_key, api_secret, testnet=True)

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {'symbol': symbol, 'side': side, 'type': order_type, 'quantity': quantity}
            if price: params['price'] = price
            
            logging.info(f"REQUEST: {params}")
            order = self.client.futures_create_order(**params)
            logging.info(f"RESPONSE: Success - {order}")
            return order
        except Exception as e:
            logging.error(f"RESPONSE: Error - {str(e)}")
            return {"error": str(e)}
