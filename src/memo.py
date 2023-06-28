def run():
    a = 100
    result = 0
    for i in range(1, 3):
        result = a >> i
        result = result + 1
    print(result)

if __name__ == '__main__':
    run();
