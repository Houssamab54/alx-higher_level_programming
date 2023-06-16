#!/usr/bin/python3

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        fields = line.strip().split(" ")
        if len(fields) >= 7:
            status_code = int(fields[5])
            file_size = int(fields[6])
            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {total_size}")
            for code, count in sorted(status_codes.items()):
                if count > 0:
                    print(f"{code}: {count}")
            sys.stdout.flush()
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")
