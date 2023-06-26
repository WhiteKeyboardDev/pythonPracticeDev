def run():
    TestList = [1, 2, 3, 4, 5]
    TestList = list(map(lambda num: num + 100, TestList))
    print(TestList)

if __name__ == '__main__':
    run();