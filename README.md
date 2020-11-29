# What is this?
A simple CLI tool to strip rows or columns from a CSV file.

# How to install
Using pip
``` pip install csv-stripper```

# How to use
This is the minimum command that will print the result to the stdout.
```sh
stripper input.csv -s n -e m
```
|---|---|
|-s, --start   |First index to start stripping.|
|-e, --end  |Last index to be stripped (included).|

Optional parameters:
|Parameter|Meaning|
|---|---|
|-o, --out   | The file to save the output.  |
|--row  |Whether the rows have to be stripped instead of the columns.   |
|-d, --delimiter   |The separator of the values.   |



