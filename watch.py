from __future__ import print_function
import sys
import time


THEMES = {
    'raw': None,
    'smallBox': (u'\u25A1', u'\u25A0'),
    'bigBox': (u'\u25A2', u'\u25A9'),
    'boxSimple': (' ', u'\u25A3'),
    'circleSimple': (' ', u'\u25C9'),
    'rhombusSimple': (' ', u'\u25C8')
}


def to_matrix(n):
    """
    convert decimal to binary matrix, at most 4 bits deep ( because 9 < 15 )
    `numpy` seems not always available, or it will be much easy to do so
    :param n: str (decimal int value)
    :return: list
    """
    tmp = ['{:0>4}'.format("{:b}".format(int(s))) for s in n]
    return [[tmp[index][i] for index in range(len(tmp))] for i in range(4)]


def theme_print(theme, text):
    for line in text:
        if THEMES.get(theme):
            print(" ".join([THEMES[theme][int(x)] for x in line]))
        else:
            print(" ".join(line))


def glimpse(theme='boxSimple', full=False, hint=False):
    t = time.localtime()
    if theme == 'basic':
        # Not So Pretty
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
    elif theme in THEMES:
        # Kinda
        if full:
            raw = '{month:0>2}{day:0>2}{week}{hour:0>2}{min:0>2}{sec:0>2}'.format(month=t.tm_mon,
                                                                                  day=t.tm_mday,
                                                                                  week=t.tm_wday + 1,
                                                                                  hour=t.tm_hour,
                                                                                  min=t.tm_min,
                                                                                  sec=t.tm_sec)
            result = to_matrix(raw)
            if hint:
                theme_print(theme, result)
                print("_" * 21)
                print('M M D D W h h m m s s')
                print(' '.join(raw))
            else:
                theme_print(theme, result)
        else:
            raw = '{hour:0>2}{min:0>2}{sec:0>2}'.format(hour=t.tm_hour, min=t.tm_min, sec=t.tm_sec)
            result = to_matrix(raw)
            if hint:
                theme_print(theme, result)
                print("_" * 11)
                print('h h m m s s')
                print(' '.join(raw))
            else:
                theme_print(theme, result)


def loop_watch(theme='basic', full=True, hint=True):
    """
    start watch click, control-C to stop
    :param theme: String
    :param full: Boolean
    :param hint: Boolean
    :return: None
    """
    try:
        while True:
            glimpse(theme, full, hint)
            if theme == 'basic':
                if full:
                    sys.stdout.write("\033[F" * 6)
                else:
                    sys.stdout.write("\033[F" * 3)
            elif theme in THEMES:
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
    loop_watch('circleSimple', hint=True, full=True)
