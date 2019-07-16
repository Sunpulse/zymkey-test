import binascii
import zymkey
from time import time, sleep
from datetime import datetime, timedelta
import signal

def sign(message):
    sig = zymkey.client.sign(message)
    return binascii.hexlify(sig)

def verify(message, signature):
    return zymkey.client.verify(message, signature)

def get_public_key():
    pub_key = zymkey.client.get_ecdsa_public_key()
    return binascii.hexlify(pub_key)

INTERVAL = 1

def main():
    print("start")
    start_time = time()
    # Test getting public key
    public_key = get_public_key()

    print("Got public key", public_key)

    # Test signing
    message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sig = sign(message)

    print("signed")

    end_time = time()
    print("done " + str(timedelta(seconds=end_time - start_time)))

def timeout_handler():
    raise Exception("Timed out")

def run_with_timeout(func, secs):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(secs)

    func()

    signal.alarm(0)

if __name__ == "__main__":
    i = 0
    while True:
        i += 1
        run_with_timeout(main, 10)
        print("i", i)

        sleep(INTERVAL - (time() % INTERVAL))
