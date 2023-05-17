class File:
    def __init__(self, msg):
        self.msg = msg

    def show(self):
        print(self.msg)

class File2:
    def __init__(self):
        self.msg = 'test Msg'

    def show(self):
        print(self.msg)

def main():
    print('hihi')
    file = File('hihi File Class')
    file.show()

if __name__ == '__main__':
    main()

