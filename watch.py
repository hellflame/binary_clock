import sys
import time


try:
    while True:
        t = time.localtime()
        print "{} | h: {:>2}".format((" " * 4).join('{:b}'.format(t.tm_hour).rjust(5)), t.tm_hour)
        print "{} | m: {:>2}".format((" " * 3).join('{:b}'.format(t.tm_min).rjust(6)), t.tm_min)
        print "{} | s: {:>2}".format((" " * 3).join('{:b}'.format(t.tm_sec).rjust(6)), t.tm_sec)
        sys.stdout.write("\033[F" * 3)
        time.sleep(.2)
except KeyboardInterrupt:
    sys.stdout.write("\n" * 3)


