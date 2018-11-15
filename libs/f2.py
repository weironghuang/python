def f2():
    print('f2')
    f1()

if __name__ != "__main__":
    from libs.f1 import f1
    from libs.readParm import parms
    print(parms)

elif __name__ == "__main__":
    from f1 import f1
    #test:
    f2()
    pass