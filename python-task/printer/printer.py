NAMED_PIPE_PATH = '/tmp/named_pipe'

def main():
    print("Printer is now running and waiting for messages...")
    with open(NAMED_PIPE_PATH, 'r') as pipe:
        while True:
            # Read a message from the named pipe
            msg = pipe.readline().strip()
            if msg:
                print("Received message:", msg)

if __name__ == "__main__":
    main()