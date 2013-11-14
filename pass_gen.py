import random
import string
import sys

def password_gen(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(letters) for i in xrange(length))

def main():
    if len(sys.argv) == 1:
        print password_gen(10)
    elif len(sys.argv) == 2:
        if sys.argv[1] in ['-h', '--help']:
            print "NAME"
            print "\t pass_gen - generate random passwords from letters, digits and punctuation"
            print "SYNOPSIS"
            print "\t pass_gen []"
            print "OPTIONS"
            print "\t -h, --help \t print this message"
            print "\t "
            print "usage: python pass_gen.py <length> (<number>)"
            sys.exit(1)
        try:
            length = int(sys.argv[1])
            print password_gen(length)
        except ValueError:
            print "cannot convert argument to integer. exiting"
            sys.exit(1)
    else:
        try:
            length = int(sys.argv[1])
            number = int(sys.argv[2])
            for i in xrange(number):
                print password_gen(length)
        except ValueError:
            print "cannot convert arguments to integer"
            print "usage: python pass_gen.py <length> (<number>)"
            sys.exit(1)

if __name__ == "__main__":
    main()
