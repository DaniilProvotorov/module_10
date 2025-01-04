import threading
import time
import queue
import random

class Table:
    guest = None
    def __init__(self, number):
        self.number = number


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        s = random.randint(3, 10)
        time.sleep(s)


import threading
from threading import Thread
import time
from queue import Queue
import random


class Table:
    guest = None
    def __init__(self, number):
        self.number = number

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        s = random.randint(3, 10)
        time.sleep(s)

class Cafe:
    q = Queue()
    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        self.guests = guests
        for guest in guests:
            seat = False
            n = 0
            for table in tables:
                n += 1
                if table.guest is None and seat == False:
                    table.guest = guest
                    seat = True
                    guest.start()
                    #guest.join()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    continue
                if table.guest is not None and seat == False and n not in range(1, 5):
                    self.q.put(guest)
                    print(f'{guest.name} в очереди')




    def discuss_guests(self):
        fr = 0
        while self.q.empty() == False or fr != 0:
            for table in tables:
                if table.guest is not None:
                    if table.guest.is_alive() == False:
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        fr +=1
                if table.guest is None:
                    table.guest = self.q.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    fr -= 1

tables = [Table(number) for number in range(1, 6)]
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
