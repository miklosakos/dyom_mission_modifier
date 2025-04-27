import sys

if len(sys.argv) < 2:
    print("Need DYOMn.dat!")
    exit(200)
elif len(sys.argv) > 2:
    print("I only need DYOMn.dat!")
    exit(200)

print(f"Working on file {sys.argv[1]}")

f = open(sys.argv[1], "rb")
bytearr = f.read(4)
f.close()

if b'\x06\x00\x00\x00' in bytearr:
    print(f"{sys.argv[1]} is in unpublished state.")
    print(f"Changing {sys.argv[1]} to published state")
    f = open(sys.argv[1], "rb+")
    f.write(b'\xfa\xff\xff\xff')
    f.close()
if b'\xfa\xff\xff\xff' in bytearr:
    print(f"{sys.argv[1]} is in published state.")
    print(f"Changing {sys.argv[1]} to unpublished state.")
    f = open(sys.argv[1], "rb+")
    f.write(b'\x06\x00\x00\x00')
    f.close()