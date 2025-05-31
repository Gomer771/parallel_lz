import asyncio

async def timer_task(duration):
    await asyncio.sleep(duration)  # приостанавливает выполнение задачи, но позволяет другим задачам выполняться параллельно
    print("Задача завершена")

async def main():
    delay = int(input("Введите количество секунд: "))  # запрашиваем время
    try:
        async with asyncio.timeout(3):  # устанавливаем тайм-аут выполнения задачи
            await timer_task(delay)
    except TimeoutError:
        print("Превышено время ожидания!")

if __name__ == "__main__":
    asyncio.run(main())  
