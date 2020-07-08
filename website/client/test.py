from client import Client
import time
from threading import Thread


c1 = Client("jes")
c2 = Client("elvo")

def update_messages():
    """
    updates the local list of msgs
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1) # update every 1/10th of sec
        new_messages = c1.get_messages()# get any new messages of client
        msgs.extend(new_messages) # add to local list of messahes
        
        for msg in new_messages: #display messages
            print(msg)
            
            if msg == "{quit}":
                run = False
                break
            
Thread(target = update_messages).start()

c1.send_message("hello")
time.sleep(3)
c2.send_message("wag1")
time.sleep(3)
c1.send_message("wuu2")
time.sleep(3)
c2.send_message("nm nm ")
time.sleep(3)
c1.disconnect()
time.sleep(3)
c2.disconnect()