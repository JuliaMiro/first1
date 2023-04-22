import time

def my_decoratortime(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        print(f"Timer start at {str(start_time)}")
        result = func(*args)
        end_time = time.perf_counter()
        time_spend = end_time - start_time
        print(f"Timer ends at {str(end_time)}")
        print(f"Function takes {str(time_spend)}")
        return result
    return wrapper()



@my_decoratortime
def power2(a):
    print(a * a)
    return a * a

power2(6)