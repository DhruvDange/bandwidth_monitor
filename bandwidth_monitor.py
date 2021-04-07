"""
**Bandwidth Monitor** - A small utility program that tracks how much data you have uploaded 
and downloaded from the net during the course of your current online session. 
"""

import psutil, time

def bytes_tracker():
    sent_old_value = 0
    recv_old_value = 0
    x = 0
    y = 0
    while True:
        bytes_recieved = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent
        if sent_old_value:
            x = bytes_sent - sent_old_value
        if recv_old_value:
            y = bytes_recieved - recv_old_value

        display_bytes(x,y)
        sent_old_value = bytes_sent
        recv_old_value = bytes_recieved
        time.sleep(1)

def display_bytes(bytes_sent, bytes_recieved):
    bytes_sent = bytes_sent/1024./1024*8
    bytes_recieved = bytes_recieved/1024./1024*8
    total_bytes = bytes_recieved + bytes_sent
    print(f"s: {'%.2f'% bytes_sent},  r: {'%.2f'% bytes_recieved}, total: {'%.2f'% total_bytes}")

bytes_tracker()