import re

byte = []
reps = []
regex = []
#\x1b\x5b\x33\x38\x3b\x35\x3b\x33\x34\x6d\x68\x6f\x73\x74\x6e\x61\x6d\x65\x1b\x5b
#  [   3   8   ;   5   ;   3   4   m   h   o   s   t   n   a   m   e     [
#regex.append(re.compile(rb"\x1b.*\x07"))
#regex.append(re.compile(rb"\x08+\x1b\x5b\x31\x34\x50"))
#regex.append(re.compile(rb"\x08(\x08)+"))
#regex.append(re.compile(rb"\x0d(\x1b\x5b\x43)+"))
#regex.append(re.compile(rb"\x1b\x5b([0-9A-Fa-f]+\x3b)+[0-9A-Fa-f]+\x6d"))
ansi_escape = re.compile(rb'\x1B\[[0-?]*[ -/]*[@-~]')

with open("/Users/tak/work/tmp/raw.txt",mode='r') as f:
    lines = f.readlines()
    for line in lines:
        byte.append(line.encode('utf-8'))
for b in byte:
    #for rep in (b"\x1b\x5b\x31\x41\x1b\x5b\x31\x4b\x1b\x5b\x4b",b"\x1b\x5b\x31\x42",b"\x1b\x5b\x3f\x31\x30\x33\x34\x68",b"\x1b\x5b\x4b"):
    #for rep in (b"\x1b\x5b\x31\x41\x1b\x5b\x31\x4b\x1b\x5b\x4b\x0d",b"\x1b\x5b\x31\x42",b"\x1b\x5b\x3f\x31\x30\x33\x34\x68",b"\x1b\x5b\x4b",b"\x1b\x5b\x30\x6d",b"\x1b\x5b\x39\x31\x6d"):
    #    b = b.replace(rep,b"")
    #for reg in regex:
    #    b = re.sub(reg,b"",b)
    b = re.sub(ansi_escape,b"",b)
    reps.append(b)

with open("/Users/tak/work/tmp/aft-raw.txt",mode='w') as af:
    for ret in reps:
        af.write(ret.decode('utf-8'))

