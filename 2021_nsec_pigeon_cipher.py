import os
from base64 import  b64decode
import string
import itertools

def chunckify(iterable, size):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk

messages = []
for root, _, files in os.walk('data/messages/'):
    for name in files:
        with open(os.path.join(root, name), 'r') as f:
            messages.append(b64decode(f.read()))


master_set = set(string.printable)

for message_subset in chunckify(messages, size=2000):
    for position in zip(*message_subset):  
        diff_set = master_set.difference({chr(value) for value in position})
        if diff_set:
            print(list(diff_set)[0], end='')
        else:
            print(' ', end='')
    print()
