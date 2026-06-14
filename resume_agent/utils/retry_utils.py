import time

def retry(func, retries=3, delay=5):

    for attempt in range(retries):

        try:
            return func()

        except Exception as e:

            print(f"Retry {attempt+1}: {e}")

            time.sleep(delay)

    return []