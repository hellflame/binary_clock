from __future__ import print_function
import sys
import time
# it seem `numpy` not always available, or it will be much easy


SMALL_BOX = (u'\u25A1', u'\u25A0')

BIG_BOX = (u'\u25A2', u'\u25A9')

BIG_BOX_SIMPLE = (' ', u'\u25A3')

THEMES = ['raw', 'smallBox', 'bigBox', 'boxSimple']


def to_matrix(n):
    """
    convert decimal to binary matrix, at most 4 bit depth ( because 9 < 15 )
    :param n: str (decimal int value)
    :return: list
    """
    tmp = ['{:0>4}'.format("{:b}".format(int(s))) for s in n]
    return [[tmp[index][i] for index in range(len(tmp))] for i in range(4)]


def line_print(theme, text):
    for line in text:
        if theme == 'smallBox':
            print(" ".join([SMALL_BOX[int(x)] for x in line]))
        elif theme == 'bigBox':
            print(" ".join([BIG_BOX[int(x)] for x in line]))
        elif theme == 'boxSimple':
            print(" ".join([BIG_BOX_SIMPLE[int(x)] for x in line]))
        else:
            print(" ".join(line))


def loop_watch(theme='basic', full=True, hint=True):
    """
    start watch click, control-C to stop
    :param theme: basic|raw|smallBox|bigBox|boxSimple
    :param full: Boolean
    :param hint: Boolean
    :return: None
    """
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
            elif theme in THEMES:
                if full:
                    raw = '{month:0>2}{day:0>2}{week}{hour:0>2}{min:0>2}{sec:0>2}'.format(month=t.tm_mon,
                                                                                          day=t.tm_mday,
                                                                                          week=t.tm_wday + 1,
                                                                                          hour=t.tm_hour,
                                                                                          min=t.tm_min,
                                                                                          sec=t.tm_sec)
                    result = to_matrix(raw)
                    if hint:
                        line_print(theme, result)
                        print("_" * 21)
                        print('M M D D W h h m m s s')
                        print(' '.join(raw))
                    else:
                        line_print(theme, result)
                else:
                    raw = '{hour:0>2}{min:0>2}{sec:0>2}'.format(hour=t.tm_hour, min=t.tm_min, sec=t.tm_sec)
                    result = to_matrix(raw)
                    if hint:
                        line_print(theme, result)
                        print("_" * 11)
                        print('h h m m s s')
                        print(' '.join(raw))
                    else:
                        line_print(theme, result)

                if hint:
                    sys.stdout.write("\033[F" * 7)
                else:
                    sys.stdout.write("\033[F" * 4)

            time.sleep(.05)
    except KeyboardInterrupt:
        if theme == 'basic':
            if full:
                sys.stdout.write("\n" * 6)
            else:
                sys.stdout.write("\n" * 3)
        elif theme in THEMES:
            if hint:
                sys.stdout.write("\n" * 7)
            else:
                sys.stdout.write("\n" * 4)


if __name__ == '__main__':
    loop_watch('boxSimple', hint=False, full=False)
