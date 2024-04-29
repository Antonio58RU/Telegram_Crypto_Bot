import multiprocessing
import time
from graphic7 import fetch_and_save_crypto_data7 as gr7

def script1():
    while True:
        print("Script 1 started")
        gr7()

def script2():
    while True:
        print("Script 2 started")
        time.sleep(1)  # Ждем 1 секунду, чтобы не забивать процессор

if __name__ == "__main__":
    # Создаем процессы для каждого скрипта
    process1 = multiprocessing.Process(target=script1)
    process2 = multiprocessing.Process(target=script2)
    
    # Запускаем оба процесса
    process1.start()
    process2.start()
    
    # Ожидаем завершения работы обоих процессов (это никогда не произойдет из-за бесконечного цикла в скриптах)
    process1.join()
    process2.join()

