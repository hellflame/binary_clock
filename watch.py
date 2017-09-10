import sys
import time


try:
    while True:
        t = time.localtime()
        print "{} | Month : {:>2}".format((" " * 7).join("{:b}".format(t.tm_mon).rjust(4)), t.tm_mon)
        print "{} |   Day : {:>2}".format((" " * 5).join("{:b}".format(t.tm_mday).rjust(5)), t.tm_mday)
        print "{} |  Week : {:>2}".format((" " * 7).join("{:b}".format(t.tm_wday + 1).rjust(4)), t.tm_wday + 1)
        print "{} |  Hour : {:>2}".format((" " * 5).join('{:b}'.format(t.tm_hour).rjust(5)), t.tm_hour)
        print "  {}   |   Min : {:>2}".format((" " * 3).join('{:b}'.format(t.tm_min).rjust(6)), t.tm_min)
        print "  {}   |   Sec : {:>2}".format((" " * 3).join('{:b}'.format(t.tm_sec).rjust(6)), t.tm_sec)
        sys.stdout.write("\033[F" * 6)
        time.sleep(.1)
except KeyboardInterrupt:
    sys.stdout.write("\n" * 6)


