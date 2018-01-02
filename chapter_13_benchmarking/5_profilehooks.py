from profilehooks import profile,timecall

@profile
def mem_func():
    lots_of_numbers = list(range(1500))
    x=['letters'] * (5**10)
    del lots_of_numbers
    return None

@timecall
def mem_func_time():
    lots_of_numbers = list(range(1500))
    x=['letters'] * (5**10)
    del lots_of_numbers
    return None

if __name__ == '__main__':
    mem_func()
    mem_func_time()