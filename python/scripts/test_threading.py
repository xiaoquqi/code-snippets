import functools
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

num_threads = 2

def run(thread_id, num=3):
    sleep_time = thread_id * 5
    print("Thread %s will sleep %s" % (thread_id, sleep_time))
    print("num = %s" % num)
    time.sleep(sleep_time)
    print("Thread %s sleep %s done" % (thread_id, sleep_time))
    return sleep_time

results = []
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for i in range(num_threads):
        future = executor.submit(run, i, num=2)
        futures.append(future)

for future in as_completed(futures):
    result = future.result()
    results.append(result)

print(results)

print("=" * 30)

def run(thread_id, num=3, index=0):
    print("Current index is %s" % index)
    sleep_time = thread_id * 5
    print("Thread %s will sleep %s" % (thread_id, sleep_time))
    print("num = %s" % num)
    time.sleep(sleep_time)
    print("Thread %s sleep %s done" % (thread_id, sleep_time))
    return sleep_time

with ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = [executor.submit(run, value, index=index) for index, value in enumerate([1, 2])]

    for future in futures:
        try:
            result = future.result()
        except Exception as e:
            # 处理异常
            print(f"An exception occurred: {e}")


#for future in as_completed(futures):
#    result = future.result()
#    print(result)

print("All Done")
