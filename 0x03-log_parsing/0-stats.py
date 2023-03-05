#!/usr/bin/python3
"""Log parsing module"""
import sys


total_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into its components
        parts = line.split()
        if len(parts) < 4:
            continue

        # Extract the file size and status code from the line
        file_size = int(parts[-1])
        status_code = parts[-2]

        # Update the statistics
        total_file_size += file_size
        if status_code in status_codes.keys():
            status_codes[status_code] += 1

        line_count += 1

        # Print statistics every 10 lines
        if line_count == 10:
            line_count = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
