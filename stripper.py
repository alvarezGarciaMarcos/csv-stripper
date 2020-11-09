#!/usr/bin/python
import click
import csv
import os

DEFAULT_OUTPUT = "stripped_"

@click.command()
@click.argument("filename", type=click.File('r')) 
@click.option('-o', "--out", type=click.Path(exists=False), help="The file where the output should be redirected.",default='-')
@click.option('-d', "--delimiter", help="The separator of the input CSV file. Defaults to ','.", default=',')
@click.option('-s', "--start", required=True, type=int, help="The starting index to strip. Starting at 0.")
@click.option('-e', "--end", required=True, type=int, help="The ending index (included) to strip.")
@click.option('--row', is_flag=True, help="Strip rows instead of columns.")
def cli(filename, out, delimiter, start, end, row):
    """
    This is a simple tool to strip columns from a CSV file
    """
    f = filename
    reader = csv.reader(filename, delimiter=delimiter)

    with click.open_file(out, 'w') as f:
        if not row:
            for row in reader:
                stripped = row[:start]
                stripped = stripped + row[end+1:]
                f.write(delimiter.join(stripped)+ '\n')
        else:
            for i, row in enumerate(reader):
                if i < start or i > end: 
                    f.write(delimiter.join(row)+ '\n')

