import sys

linecount = 0

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".py"):
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if line.lstrip().startswith("#"):
                        pass
                    elif len(line.lstrip())<1:
                        pass
                    else:
                        linecount += 1
                print(linecount)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
