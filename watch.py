from __future__ import print_function
import sys
import time

SMALL_BOX_EMPTY = u'\u25A1'
SMALL_BOX_FULL = u'\u25A0'

BIG_BOX_EMPTY = u'\u25A2'
BIG_BOX_FULL = u'\u25A9'


def loop_watch(full=True, theme='basic', hint=True):
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
            elif theme == 'smallBox':
                pass
            time.sleep(.1)
    except KeyboardInterrupt:
        if theme == 'basic':
            if full:
                sys.stdout.write("\n" * 6)
            else:
                sys.stdout.write("\n" * 3)


if __name__ == '__main__':
    loop_watch(hint=False)
