'''
FPP library
'''
from time import sleep
from typing import List


class Peripheral:
    def __init__(self, device_path) -> None:
        self.device_path = device_path

        print(f"Peripheral initialized with device path: {device_path}")


class Listener:
    def on_massage_received(self, msg):
        raise NotImplementedError("The method should be overriden")
    

class Notifire:
    def __init__(self, peripheral: Peripheral, listeners: List[Listener]):
        self.peripheral = peripheral
        self.listeners = listeners
        print("Notifire initialized")

    def run(self):
        """Continuously reads messages from the peripheral and notifies listeners."""
        self.running = True
        print("Notifire is running...")
        
        while self.running:

            # Read message from peripheral
            msg = self.peripheral.read_message()

            # Notify each listener
            for listener in self.listeners:
                listener.on_message_received(msg)

            sleep(1)

    def sleep(self):
        self.running = False
        print("Notifire has stopped.")