#-------Libraries-------
import websocket
import json
#-------Setup-------
ws=websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=10&encoding=json")
#-------Code-------
def login(ws,request):
    ws.send(json.dump(request))

def logger(ws):
    response=ws.recv()
    if response:
        return json.load(response)

token=""

payloads={
    "op":2,
    "d":{
        "token":token,
        "intents":513,
        "properties":{
            "$os":'linux',
            "$browser":'Nuwa',
            "device":'Nuwa'
        }
    }
}

login(ws,payloads)