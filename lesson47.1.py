from random import randint
from time import sleep
import threading

lock = threading.Lock()

class Bank:
    def __init__(self, balance: int, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(0, 100):
            random_number = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_number
            print(f'Пополнение: {random_number}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range (0, 100):
            random_number = randint(50, 500)
            print(f'Запрос на снятие: {random_number}')
            if random_number <= self.balance:
                self.balance -= random_number
                print(f'Снятие: {random_number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


Morgan_Stanley = Bank(0, lock)
th1 = threading.Thread(target=Morgan_Stanley.deposit(), args=(Morgan_Stanley,))
th2 = threading.Thread(target=Morgan_Stanley.take(), args=(Morgan_Stanley,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {Morgan_Stanley.balance}')