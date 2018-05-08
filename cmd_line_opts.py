# Command-line options are very useful, early on, to identify the use cases.

import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv[1:], "ho:", ["help", "output="])
    except getopt.GetoptError as e:
        print e
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print "Usage : " + argv[0], "-h -o <output file>"
            sys.exit()
        elif opt in ('-o', '--output'):
            print "output =", arg

# usage
if __name__ == '__main__':
    main(sys.argv)
