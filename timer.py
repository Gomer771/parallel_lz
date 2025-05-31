import multiprocessing

def update_counter(counter, lock, result_list):
    for _ in range(1000):
        with lock:
            counter.value += 1 #увеличиваем значение счётчика
            result_list.append(counter.value) #добавляем текущее значение счётчика в общий список

def main():
    lock = multiprocessing.Lock() #объект для синхронизации доступа к counter
    counter = multiprocessing.Value('i', 0) #общий счётчик, который хранит значение 
    manager = multiprocessing.Manager() #менеджер, для работы процессоров с общими объектами
    result_list = manager.list() #список для хранения значений счётчика


    processes = [multiprocessing.Process(target=update_counter, args=(counter, lock, result_list)) for _ in range(10)] #список с 10-ю процессами

    for proc in processes:
        proc.start() #запускаем процесс
    for proc in processes:
        proc.join() #ожидаем завершения всех процессов перед продолжением выполнения

    print(result_list)

if __name__ == '__main__':
    main()
