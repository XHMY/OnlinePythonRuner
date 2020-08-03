with open("demo/test.py") as fd:
    code = fd.readlines()

for l in code:
    if l[:7] == "import ":
        exec(l)
    elif l == '\n':
        continue
    else:
        x = eval(l)
