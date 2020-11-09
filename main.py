import hashlib
import itertools
import time
import string
import sys
from multiprocessing import Pool, Lock


all_chars = string.printable
more_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@"
select_chars = "1234ADZGCTFOPEodbranjghtsw@"
hashes = [line.rstrip('\n') for line in open("hashes.txt")]
start = time.perf_counter()


def iterate(i):
    for new_string in itertools.product(select_chars, repeat=i):
        cur_pass = ''.join(new_string)
        hash_check = hashlib.md5(cur_pass.encode())
        if hash_check.hexdigest() in hashes:
            print(f'{cur_pass} was cracked in {time.perf_counter() - start:0.5f} seconds')


if __name__ == '__main__':
    with Pool() as pool:
        pool.map(iterate, range(1, len(max(hashes, key=len)) + 1))
