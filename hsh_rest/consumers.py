from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from pudb import set_trace
class EventEntryConsumer(WebsocketConsumer):
    groups = ["model_updates"]
    #channel = 'model_updates'
    def connect(self):
        # Called on connection.
        # To accept the connection call:
        # set_trace()
        async_to_sync(self.channel_layer.group_add)("model_updates", self.channel_name)
        self.accept()   

    def receive_update(self, text=None):
        print("ASDASD")
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data=json.dumps(text))
        # Or, to send a binary frame:


    def disconnect(self, close_code):
        # Called when the socket closes
        async_to_sync(self.channel_layer.group_discard)("model_updates", self.channel_name)
