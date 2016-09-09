import time

strs = []
increaseByMBPerSecond = 10
while True:
    print len(strs)
    strs.append(' ' * increaseByMBPerSecond * (2 ** 20))
    time.sleep(3)
