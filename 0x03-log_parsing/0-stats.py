#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code

After every 10 lines and on keyboard interruption, prints the statistics.
"""
import re
import sys


def print_stats(total_size, status_counts):
    """Print the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin and compute metrics every 10 lines or on interrupt."""
    pattern = re.compile(
        r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[.+\] '
        r'"GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
    )
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    status_counts = {code: 0 for code in valid_codes}
    total_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            match = pattern.match(line.strip())
            if match:
                try:
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))
                    total_size += file_size
                    if status_code in valid_codes:
                        status_counts[status_code] += 1
                except (ValueError, IndexError):
                    continue

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
