def main():
    sentence = input()
    print(convert(sentence))

def convert(line):
    return (line.replace(':)', '🙂').replace(':(', '🙁'))

main()
