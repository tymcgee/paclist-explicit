# Paclist-explicit
Get a list of explicitly installed pacman packages sorted by date.

Explicitly installed packages are specified by the output of `pacman -Qe`.
Install dates are specified in `pacman.log`.

# Usage
`python paclist-explicit.py`

There are no arguments.

## Example output:
```
...
[2023-10-12T19:54:19-0700] [ALPM] installed jq (1.7-1)
[2023-10-14T13:08:00-0700] [ALPM] installed httpie (3.2.1-4)
[2023-10-18T19:38:42-0700] [ALPM] installed docker-buildx (0.11.2-1)
[2023-10-28T13:04:07-0700] [ALPM] installed node-gyp (9.4.0-1)
[2023-11-01T21:41:43-0700] [ALPM] installed ncspot (0.13.2-3)
[2023-11-02T23:34:19-0700] [ALPM] installed fzf (0.43.0-1)
[2023-11-09T21:42:33-0800] [ALPM] installed cloc (1.98-1)
...
```

# Warning
This was written in 20 minutes and is not guaranteed to work as described.
It's good enough for my own purposes.

# License
The UNLICENSE
