import hashlib
import itertools
import time
import string
from multiprocessing import Pool, Lock


# select_chars = "1234ADZGCTFOPEodbranjghtsw@"
hashes = [line.rstrip('\n') for line in open("hashes.txt")] # read hashes into array
start = time.perf_counter() # start time counter


def iterate(i):
    # iterate over every cross product of chars at the given index of printable character length
    for new_string in itertools.product(string.printable, repeat=i):
        cur_pass = ''.join(new_string)
        hash_check = hashlib.md5(cur_pass.encode()) # hash the password
        if hash_check.hexdigest() in hashes: # check if the hash matches a password and ouput time if yes
            print(f'{cur_pass} was cracked in {time.perf_counter() - start:0.5f} seconds')


if __name__ == '__main__':
    # use multiprocessing on multiple cores (given by sys.cpu_count()) to speed up cracking
    with Pool() as pool:
        pool.map(iterate, range(1, len(max(hashes, key=len)) + 1))
