#!/usr/bin/python3
""" kjshjkhskjshkjdhjh """
import sys


status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
total_size = 0
read_lines = 0
status_hash = {}


def print_stats():
    """kljsakljs klsjakasj """
    print(f"File size: {total_size}")
    for key, value in sorted(status_hash.items()):
        if value:
            print(f"{key}: {value}")


try:
    for line in sys.stdin:
        args = line.split()
        if len(args) == 9:
            try:
                status_code = int(args[-2])
                if status_code in status_codes:
                    status_hash[status_code] = status_hash.get(status_code, 0) + 1
                    file_size = int(args[-1])
                    total_size += file_size
            except  (IndexError, ValueError, TypeError):
                continue
        read_lines += 1
        if read_lines % 10 == 0:
            print_stats()
    print_stats()

except KeyboardInterrupt:
    print_stats()
