import threading
import time

def timer(duration):
    time.sleep(duration) #приостанавливает выполнение 
    print("Задача завершена")

def run(func, args=(), timeout=3): #максимальное время ожидания выполнения потока (3 сек.)
    thread = threading.Thread(target=func, args=args) #создаём новый поток
    thread.start() #запускаем поток
    thread.join(timeout) #ожидаем завершения потока
    if thread.is_alive(): #проверяем работает ли поток после истечения времени
        print("Превышено время ожидания")
        thread.join() 

time = int(input("Введите количество секунд: ")) #запрашиваем время
run(timer, args=(time,), timeout=3)
