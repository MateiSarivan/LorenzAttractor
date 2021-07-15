import sys
from lorat.lorat import main



if __name__ == '__main__':

    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()