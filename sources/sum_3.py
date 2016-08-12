def run():
    while True:
        str_input = raw_input()
        a, b = map(int, str_input.split())

        if a != 0 and b != 0:
            print a + b
        else:
            break
        

if __name__ == '__main__':
    run()
