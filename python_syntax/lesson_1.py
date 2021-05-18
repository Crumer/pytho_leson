a = 10
b = 5

if a > b:
    print("A > B")
    print(a - b)
else:
    print("B >/= A")
    print(b - a)

print("and")

def open_file(filename):
    print("read file", filename)
    with open(filename) as f:
        return f.read()
        print("ok")