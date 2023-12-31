#!/usr/bin/python3
"""
Module reads from stdin
"""

import sys


def print_stats(total: int, status_code: dict) -> None:
    """
    function aids main function in printing stats
    """
    print(f"File size: {total}")
    for code, count in sorted(status_code.items()):
        print(f"{code}: {count}")


def read_from_stdin() -> None:
    """
    main function that reads lines from stdin
    """
    line_count = 0
    total_size = 0
    status_code_count = {}

    # print_stats(total_size, status_code_count)

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split(" ")
            if len(parts) < 7:
                continue

            status_code = parts[-2]
            try:
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_code_count[status_code] = status_code_count.get(status_code, 0) + 1  # noqa
            except ValueError:
                pass

            file_size = parts[-1]
            try:
                file_size = int(file_size)
                total_size += file_size
            except ValueError:
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_code_count)
    except KeyboardInterrupt:
        print_stats(total_size, status_code_count)


if __name__ == '__main__':
    read_from_stdin()
