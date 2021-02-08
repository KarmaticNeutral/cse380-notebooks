def choose(n, k):
    p = 1    
    for i in range(1, min(k, n - k) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def num_2s_prime_fac(x):
    #print(x)
    prime = 2
    count = 0 
    val = prime
    while (True): 
        a = x // val
        b = (x - 1) // val
        val *= prime
        if (a - b): 
            count += (a - b)
        else: 
            break
    return int(count)


def test_conjecture(n):
    a = bin(n).count("1") 
    b = num_2s_prime_fac(choose(2*n, n))
    return a == b


def verify_block(current_number, block_size):
    for n in range(current_number, current_number + block_size):
        if not test_conjecture(n):
            print("FALSE AT ", n)

from datetime import datetime, timedelta

current_date = datetime.now()
start_date = datetime.now()
end_date = datetime.now() + timedelta(hours = 24)

print("Start Time: ", start_date)
print("Intended End Time: ", end_date)

block_size = 100
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