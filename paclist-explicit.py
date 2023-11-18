#!/usr/bin/env python

"""
Tynan McGee
November 17, 2023
License: The UNLICENSE

Using the pacman log file located at /var/log/pacman.log, find all package
installs and then filter them down to only the ones that were explicitly
installed (the ones listed by pacman -Qe). By virtue of it filtering down by
the output of pacman -Qe, previously removed packages which appear in the
pacman log file will not appear in the output.
"""

import sys
import subprocess
from pathlib import Path


def main():
    installed_lines = []
    pacman_log_file = Path("/var/log/pacman.log")
    if not pacman_log_file.exists:
        print("Could not find pacman log file at /var/log/pacman.log. Sorry")
        sys.exit(1)

    with open("/var/log/pacman.log", "r") as log:
        for line in log:
            if "[ALPM] installed" in line:
                # [:-1] removes the newline character at the end
                installed_lines.append(line[:-1])

    explicitly_installed = []
    r = subprocess.run(["pacman", "-Qe"], capture_output=True)
    # [:-1] removes the blankline at the end
    explicitly_installed = [line for line in r.stdout.decode().split("\n")][:-1]

    by_date = []
    for line in installed_lines:
        for e in explicitly_installed:
            # e looks like package-name (version), so e.split(" ")[0] is package-name.
            # line looks like [iso-datestring] [ALPM] installed package-name (version),
            # so line.split(" ")[3] is package-name.
            if e.split(" ")[0] == line.split(" ")[3]:
                by_date.append(line)

    # Sometimes the installed num is different from the found by date. I wouldn't
    # expect that to be the case, but alas, I wrote this in 20 minutes and it works
    # well enough for my purposes.
    print("Num of explicitly installed packages:", len(explicitly_installed))
    print("Num of installed packages:", len(installed_lines))
    print("Num of installed packages filtered by explicit installation:", len(by_date))
    for line in by_date:
        print(line)


if __name__ == "__main__":
    main()
