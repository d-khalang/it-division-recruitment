import os
from fpp import Listener

NAMED_PIEP_PATH = '/tmp/named_pipe'

# Make sure named pipe exist
if not os.path.exists(NAMED_PIEP_PATH):
    os.mkfifo(NAMED_PIEP_PATH)


class CustomListener(Listener):
    def on_message_received(self, msg):
        # writing messages to the named pipe
        with open(NAMED_PIEP_PATH, 'w') as pipe:
            pipe.write(msg + '\n')
