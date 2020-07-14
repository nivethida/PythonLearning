class First(object):
    def _init_(self):
        print("first")

class Second(object):
    def _init_(self):
        print("second")

class Third(First, Second):
    def _init_(self):
        super(Third, self)._init_()
        print("that's it")

    if __name__ == '__main__':
        c = Third()

