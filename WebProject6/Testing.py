
import requests
import websocket, json

###### Get request Test (remove the hash tags and hashtag the other "def" functions to try this one) #########
# 
#response = requests.get("http://randomfox.ca/floof")
#fox = response.json()

#print(fox)
#print(fox['link'])



#### Stream of 'BTC-USD' ....... 

##TRY ADDING:, "ETH-USD"      in same line after the "BTC-USD" portion of this payload

def on_open(ws):
    print("opened connection")

    subscribe_message = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD"
                ]
            }
        ]
    }
    ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
    print("received message")
    print(message)




socket = "wss://ws-feed.pro.coinbase.com"

ws = websocket.WebSocketApp(socket,on_open=on_open, on_message=on_message)
ws.run_forever()


##List of Data Available through API for each Ticker##             ??Possibly Different Types??


##{'type': 'ticker', 
#'sequence': 29275941194, 
#'product_id': 'BTC-USD',
#'price': '46627.73', 
#'open_24h': '45072.53',
#'volume_24h': '11894.31109525', 
#'low_24h': '44679.92',
#'high_24h': '46976.12', 
#'volume_30d': '347243.18247575',
#'best_bid': '46627.73', 
#'best_ask': '46627.74',
#'side': 'sell',
#'time': '2021-09-14T22:02:51.704445Z' 
#'trade_id': 211441192,
#'last_size': '0.00718232'}

#################################################################

##message original####
##{'type': 'ticker', 'sequence': 29276017582, 'product_id': 'BTC-USD', 'price': '46745.62', 'open_24h': '45072.53', 'volume_24h': '11914.06841909', 'low_24h': '44679.92', 'high_24h': '46976.12', 'volume_30d': '347262.93979959', 'best_bid': '46745.61', 'best_ask': '46745.62', 'side': 'buy', 'time': '2021-09-14T22:05:50.641119Z', 'trade_id': 211441774, 'last_size': '0.00002256'}





###END



859.95","side":"sell","time":"2021-09-15T14:07:10.002402Z","trade_id":211633952,"last_size":"0.00149412"}
received message
{"type":"ticker","sequence":29296554277,"product_id":"BTC-USD","price":"47855.64","open_24h":"46589.3","volume_24h":"11923.82623327","low_24h":"46338.23","high_24h":"47921","volume_30d":"344184.09414824","best_bid":"47855.64","best_ask":"47859.95","side":"sell","time":"2021-09-15T14:07:10.002402Z","trade_id":211633953,"last_size":"0.00135308"}
received message
{"type":"ticker","sequence":20794514765,"product_id":"ETH-USD","price":"3442.84","open_24h":"3345.72","volume_24h":"131455.54288622","low_24h":"3331.93","high_24h":"3452.06","volume_30d":"5654625.53298123","best_bid":"3442.83","best_ask":"3442.84","side":"buy","time":"2021-09-15T14:07:10.086958Z","trade_id":155943158,"last_size":"0.00679239"}
received message
{"type":"ticker","sequence":20794514791,"product_id":"ETH-USD","price":"3442.84","open_24h":"3345.72","volume_24h":"131455.67924675","low_24h":"3331.93","high_24h":"3452.06","volume_30d":"5654625.66934176","best_bid":"3442.83","best_ask":"3442.84","side":"buy","time":"2021-09-15T14:07:10.326944Z","trade_id":155943159,"last_size":"0.13636053"}
received message
{"type":"ticker","sequence":20794514793,"product_id":"ETH-USD","price":"3442.84","open_24h":"3345.72","volume_24h":"131455.82792954","low_24h":"3331.93","high_24h":"3452.06","volume_30d":"5654625.81802455","best_bid":"3442.83","best_ask":"3442.84","side":"buy","time":"2021-09-15T14:07:10.326944Z","trade_id":155943160,"last_size":"0.14868279"}
received message