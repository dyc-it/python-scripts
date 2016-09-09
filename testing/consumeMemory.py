import sys
import time


def consume_memory(v_increase_by_mb_per_second):
    strs = []

    while True:
        print len(strs)
        strs.append(' ' * int(v_increase_by_mb_per_second) * (2 ** 20))
        time.sleep(1)


if __name__ == "__main__":
    increase_by_mb_per_second = 10

    if len(sys.argv) == 2:
        increase_by_mb_per_second = sys.argv[1]

    consume_memory(increase_by_mb_per_second)
