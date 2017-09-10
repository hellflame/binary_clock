from __future__ import print_function
import sys
import time
# it seem `numpy` not always available, or it will be much easy


SMALL_BOX_EMPTY = u'\u25A1'
SMALL_BOX_FULL = u'\u25A0'

BIG_BOX_EMPTY = u'\u25A2'
BIG_BOX_FULL = u'\u25A9'


def to_matrix(n):
    """
    convert decimal to binary matrix, at most 4 bit depth ( because 9 < 15 )
    :param n: str (decimal int value)
    :return: list
    """
    tmp = ['{:0>4}'.format("{:b}".format(int(s))) for s in n]
    return [[tmp[index][i] for index in range(len(tmp))] for i in range(4)]


def loop_watch(theme='basic', full=True, hint=True):
    try:
        while True:
            t = time.localtime()
            if theme == 'basic':
                if full:
                    if hint:
                        print("{} | Month : {:>2}".format((" " * 7).join("{:b}".format(t.tm_mon).rjust(4)), t.tm_mon))
                        print("{} |   Day : {:>2}".format((" " * 5).join("{:b}".format(t.tm_mday).rjust(5)), t.tm_mday))
                        print("{} |  Week : {:>2}".format((" " * 7).join("{:b}".format(t.tm_wday + 1).rjust(4)),
                                                          t.tm_wday + 1))
                    else:
                        print("{}".format((" " * 7).join("{:b}".format(t.tm_mon).rjust(4))))
                        print("{}".format((" " * 5).join("{:b}".format(t.tm_mday).rjust(5))))
                        print("{}".format((" " * 7).join("{:b}".format(t.tm_wday + 1).rjust(4))))
                else:
                    if hint:
                        print("{} |  Hour : {:>2}".format((" " * 5).join('{:b}'.format(t.tm_hour).rjust(5)), t.tm_hour))
                        print("  {}   |   Min : {:>2}".format((" " * 3).join('{:b}'.format(t.tm_min).rjust(6)), t.tm_min))
                        print("  {}   |   Sec : {:>2}".format((" " * 3).join('{:b}'.format(t.tm_sec).rjust(6)), t.tm_sec))
                    else:
                        print("{}".format((" " * 5).join('{:b}'.format(t.tm_hour).rjust(5))))
                        print("  {}   ".format((" " * 3).join('{:b}'.format(t.tm_min).rjust(6))))
                        print("  {}   ".format((" " * 3).join('{:b}'.format(t.tm_sec).rjust(6))))

                if full:
                    sys.stdout.write("\033[F" * 6)
                else:
                    sys.stdout.write("\033[F" * 3)
            elif theme == 'raw':
                if full:
                    raw = '{month:0>2}{day:0>2}{week}{hour:0>2}{min:0>2}{sec:0>2}'.format(month=t.tm_mon,
                                                                                          day=t.tm_mday,
                                                                                          week=t.tm_wday + 1,
                                                                                          hour=t.tm_hour,
                                                                                          min=t.tm_min,
                                                                                          sec=t.tm_sec)
                    result = to_matrix(raw)
                    if hint:
                        for i in result:
                            print(" ".join(i))
                        print("_" * 21)
                        print('M M D D W h h m m s s')
                        print(' '.join(raw))
                    else:
                        for i in result:
                            print(" ".join(i))
                else:
                    raw = '{hour:0>2}{min:0>2}{sec:0>2}'.format(hour=t.tm_hour, min=t.tm_min, sec=t.tm_sec)
                    result = to_matrix(raw)
                    if hint:
                        for i in result:
                            print(" ".join(i))
                        print("_" * 11)
                        print('h h m m s s')
                        print(' '.join(raw))
                    else:
                        for i in result:
                            print(" ".join(i))

                if hint:
                    sys.stdout.write("\033[F" * 7)
                else:
                    sys.stdout.write("\033[F" * 4)


            time.sleep(.1)
    except KeyboardInterrupt:
        if theme == 'basic':
            if full:
                sys.stdout.write("\n" * 6)
            else:
                sys.stdout.write("\n" * 3)
        elif theme == 'raw':
            if hint:
                sys.stdout.write("\n" * 7)
            else:
                sys.stdout.write("\n" * 4)


if __name__ == '__main__':
    loop_watch('raw', hint=True, full=False)
