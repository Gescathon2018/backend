from channels.generic.websocket import JsonWebsocketConsumer


class BSConsumer(JsonWebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        # account = text_data['account']
        # mode = text_data['mode']
        # leds = text_data['leds']

        print(self.__dict__)

        print('*'*90)
        print(text_data)
        print('*'*90)

        self.send(text_data=text_data)