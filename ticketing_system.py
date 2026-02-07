import time
import random
from datetime import datetime
from collections import deque

class Ticket:
    def __init__(self, number):
        self.number = number
        self.timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

queue = deque()
next_number = 1

def generate_tickets(count):
    global next_number
    for _ in range(count):
        time.sleep(random.uniform(0.5, 1.5))
        t = Ticket(next_number)
        next_number += 1
        queue.append(t)
        print(f"Generated Ticket #{t.number} at {t.timestamp}")

def process_tickets():
    if not queue:
        print("No tickets to serve.")
        return

    while queue:
        time.sleep(random.uniform(0.5, 1.5))
        t = queue.popleft()
        print(f"Serving Ticket #{t.number} (created at {t.timestamp})")
