import sys

# print(sys.version)
# print(sys.version_info)
# print(sys.platform)
# print(sys.winver)
# print(sys.path)
# print(sys.stdout.write("Working with sys module"))

# print(sys.stdin)
# print(sys.stdin.readline())
for line in sys.stdin:
    print(line.rstrip())
    print(line.upper())