from pprint import pprint

val_dict = [{'dec' : i, 'bin' : bin(i), 'oct' : oct(i), 'hex' : hex(i)} for i in range(16)]

pprint(val_dict)
