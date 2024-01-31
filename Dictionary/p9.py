#Check order of character in string using OrderedDict( )

from collections import OrderedDict

def check_order(string, pattern):
    dict_string = OrderedDict.fromkeys(string)
    return ''.join(dict_string.keys()) == pattern

# Example
string = 'hello world'
pattern = 'hlo'
result = check_order(string, pattern)
print(result)
