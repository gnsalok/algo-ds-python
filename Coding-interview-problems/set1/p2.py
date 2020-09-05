"""
Problem : Return true if target is present is source (string problem)
Author : Alok Tripathi

"""


source = 'abcde'
target = 'ab'

print(f'"{source}" contains "{target}" = {target in source}')

if target in source:
    print(f'"{source}" contains "{target}"')
else:
    print(f'"{source}" does not contain "{target}"')
