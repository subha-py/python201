import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might want to put example usage"
    )
    #required argument
    parser.add_argument('-x',action='store',required=True,help='Help text for option x')

    #optional arguments
    parser.add_argument('-y',help='help text for option Y',default=False)
    parser.add_argument('-z',help='help text for option Z',type=int)
    return parser.parse_args()


if __name__ == '__main__':
    get_args()
