import threading
import time                      
counter = 0

NUM_THREADS = 8                  
INCREMENTS = 20_000              


def worker():
    global counter
    for _ in range(INCREMENTS):
        tmp = counter            
        time.sleep(0)    # CPython GIL 뺏기는 상황 대비(요즘 python interpretor가 기본적으로 락을 걸거나 스레드 연산속도가 너무빨라 레이스 컨디션이 발생안함)       
        counter = tmp + 1        


def main():
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker)
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    expected = NUM_THREADS * INCREMENTS
    print(f"기대값 (expected): {expected}")
    print(f"실제값 (actual):   {counter}")
    print(f"사라진 갱신:        {expected - counter}")


if __name__ == "__main__":
    main()