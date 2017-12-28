import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might want to put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action='store', help='Help text for x')
    group.add_argument('-y', help='help text for option y', default=False)
    parser.add_argument('-z', help='help text for option z', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    # correct way to treat arguments
    values = vars(args)
    print(values)
