import hashlib
import itertools
import time
import threading


def iterate(i, start_time):
    for new_string in itertools.product("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@", repeat=i):
        cur_pass = ''.join(new_string)
        hash_check = hashlib.md5(cur_pass.encode())
        if hash_check.hexdigest() in hashes:
            print(f'{cur_pass} was cracked in {time.perf_counter() - start_time:0.5f} seconds')


hashes = []
with open("hashes.txt") as file:
    for line in file.readlines():
        hashes.append(line.rstrip())
file.close()
start = time.perf_counter()
for x in range(1, len(max(hashes, key=len)) + 1):
    # threading.Thread(target=iterate, args=(x, start)).start()
    iterate(x, start)
