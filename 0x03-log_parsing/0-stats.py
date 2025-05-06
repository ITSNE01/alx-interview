#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

""" Initialize metrics """
total_size = 0
status_codes = defaultdict(int)
line_count = 0


def print_metrics():
    """ Prints the current metrics. """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """ Handles keyboard interruption (CTRL+C). """
    print_metrics()
    sys.exit(0)


""" Register the signal handler for keyboard interruption """
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        
        """ Parse the line """
        parts = line.split()
        if len(parts) != 7:
            continue  # Skip lines that do not match the format

        ip_address, date, method, path, protocol, status_code, file_size = (
            parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]
        )

        """ Validate the status code and file size """
        if status_code.isdigit() and file_size.isdigit():
            status_code = int(status_code)
            file_size = int(file_size)

            """ Only count valid status codes """
            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                total_size += file_size
                status_codes[status_code] += 1

        """ Print metrics every 10 lines """
        if line_count % 10 == 0:
            print_metrics()

except Exception as e:
    print(f"Error: {e}")
