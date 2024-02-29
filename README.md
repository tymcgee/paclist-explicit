# Paclist-explicit
Get a list of explicitly installed pacman packages sorted by date.

Explicitly installed packages are specified by the output of `pacman -Qe`.
Install dates are specified in `pacman.log`.

# Usage
`python paclist-explicit.py`

Arguments:
| Argument                         | Purpose                                                             |
|----------------------------------|---------------------------------------------------------------------|
| -d --hide-date                   | Hide the date from appearing in the output                          |
| --date-format {iso,ymd,friendly} | Choose the format for the date (iso, yyyy-mm-dd, or friendly)       |
| -v --verbose                     | Show some debug information at the top before the list gets printed |
| -s --show-version                | Show package versions next to their names                           |

## Example output:
```
...
2023-05-29 lightdm 
2023-05-29 lightdm-webkit2-greeter 
2023-05-29 lightdm-webkit-theme-litarvan 
2023-05-29 bat 
2023-05-29 gnome-keyring 
2023-05-30 opusfile 
2023-05-30 gst-plugins-base 
2023-11-19 eza 
2023-11-19 go 
2024-02-28 tectonic
...
```

# License
The UNLICENSE
