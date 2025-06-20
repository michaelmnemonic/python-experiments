# this fails with a TypeError exception
try:
    print("Hallo" + 13)
except TypeError:
    print("This produces a TypeError")
except:
    print("Something broke")