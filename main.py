import time

from binance import ThreadedWebsocketManager

api_key = 'DqeufG2sOJhNzbzrEGHeT1ISZQN86BhGzUjPgDqO1cW4mP85ezoBQCkgCcCAQFWB'
api_secret = 'G1U32vVN8XBmCy3tyhouCdxumzsu1MN8KyDIogJlGCrZtAnYi3DQ1wijRCClWZr8'
last_update_1 = 0
last_update_2 = 0

def main():
    symbol = 'BNBBTC'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        global last_update_1
        global last_update_2

        data_basic = msg["stream"].split("@")
        pair_name = data_basic[0]
        pair_interval = data_basic[1]
        pair_current_update = float(msg['data']['k']['T'])
        if pair_current_update > last_update_1 and pair_name == "bnbbtc":
            last_update_1 = pair_current_update
            print(pair_name)
        if pair_current_update > last_update_2 and pair_name == "bnbusdt":
            last_update_2 = pair_current_update
            print(pair_name)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['bnbbtc@kline_5m', 'bnbusdt@kline_5m']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


if __name__ == "__main__":
   main()