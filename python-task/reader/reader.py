import threading
from time import sleep
from fpp import Peripheral, Notifire
from custom_listener import CustomListener

DEVICE_PATH = '/dev/sensor'

def main():
    # start the pripheral
    peripheral = Peripheral(device_path=DEVICE_PATH)

    listener = CustomListener()

    notifire = notifire(peripheral, [listener])

    # Start notifire on a seperated thread
    notifire_thread = threading.Thread(target=notifire.run)
    notifire_thread.start()


    # to run it for a minute
    sleep(60)

    notifire.stop()
    notifire_thread.join() 

if __name__ == "__main__":
    main()

