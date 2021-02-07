from numba import jit

@jit
def num_2s_prime_fac(n):
    x = n
    num_2s = 0
    while x % 2 == 0:
        num_2s = num_2s + 1
        x = x / 2
    return num_2s

@jit
def conjecture(m):
    o = m / 2 ** num_2s_prime_fac(m)
    return o % 2 == 1 and o > 0

@jit
def verify_block(current_number, block_size):
    for n in range(current_number, current_number + block_size):
        if not conjecture(n):
            print("FALSE AT ", n)
            break

from datetime import datetime, timedelta

current_date = datetime.now()
start_date = datetime.now()
end_date = datetime.now() + timedelta(hours = 24)

print("Start Time: ", start_date)
print("Intended End Time: ", end_date)

block_size = 10000000
current_number = 1

while(current_date < end_date):
    verify_block(current_number, block_size)
    current_number += block_size
    current_date = datetime.now()
    print(current_number, current_date)

actual_stop = datetime.now()
print("Final Count: ", current_number)

with open("../Final Info.txt", "w") as f:
    f.write("Final Count: " + str(current_number) + "\n")
    f.write("Start Time: " + str(start_date) + "\n")
    f.write("Intended End Time: "+ str(end_date) + "\n")   
    f.write("Actual End Time: " + str(actual_stop))     