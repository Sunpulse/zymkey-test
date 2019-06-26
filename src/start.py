import binascii
import zymkey
from time import time, sleep
from datetime import datetime, timedelta

def sign(message):
    sig = zymkey.client.sign(message)
    return binascii.hexlify(sig)

def verify(message, signature):
    return zymkey.client.verify(message, signature)

def get_public_key():
    pub_key = zymkey.client.get_ecdsa_public_key()
    return binascii.hexlify(pub_key)

INTERVAL = 60

def main():
    print("Start publishing messages")
    start_time = time()
    public_key = get_public_key()

    print("Got public key")

    end_time = time()
    print("done " + str(timedelta(seconds=end_time - start_time)))

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print("main error", e)
        sleep(INTERVAL - (time() % INTERVAL))
