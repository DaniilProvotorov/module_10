import threading
import random
import time

class Bank:
    lock = threading.Lock()
    balance = 0
    n = 100

    def deposit(self):
        while self.n:
            self.n -= 1
            s = random.randint(50, 500)
            self.balance += s
            print(f'Пополнение: {s}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        while self.n:
            self.n -= 1
            s = random.randint(50, 500)
            print(f'Запрос на {s}')
            if s <= self.balance:
                self.balance -= s
                print(f'Снятие: {s}. Баланс: {self.balance}')
            if s > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args= (bk,))
th2 = threading.Thread(target=Bank.take, args= (bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс:{bk.balance}')

