import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.n = 100

    def run(self):
        print(f'{self.name}, на нас напали!', end='\n')
        t = 0
        while self.n:
            time.sleep(1)
            dil = 1
            t += dil
            self.n -= self.power
            print(f'{self.name} сражается {t} дней(дня), осталось {self.n} воинов.', end='\n')
        print(f'{self.name}одержал победу спустя {t} дней(дня)!', end='\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()