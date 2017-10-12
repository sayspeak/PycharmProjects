
def main():
    fname = eval(input("filename："))
    infile = open(fname, "r")
    data = infile.read()
    print(data)
main()