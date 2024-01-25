#!/usr/bin/python3
import sys

if __name__ == "__main__":
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    total_size = 0
    read_lines = 0
    status_hash = {}
    try:
        for line in sys.stdin:
            args = line.split()
            if len(args) == 9:
                status_code = int(args[-2])
                if status_code in status_codes:
                    status_hash[status_code] = status_hash.get(status_code, 0) + 1
                    file_size = int(args[-1])
                    total_size += file_size
            read_lines += 1
            if read_lines % 10 == 0:
                print(f"File size: {total_size}")
                sorted_status_hash = {key: status_hash.get(key) for key in status_codes}
                for key, value in sorted_status_hash.items():
                    if value:
                        print(f"{key}: {value}")
    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for key, value in sorted_status_hash.items():
            if value:
                print(f"{key}: {value}")
        raise

