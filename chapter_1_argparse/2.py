import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might want to put example usage"
    )
    return parser.parse_args()


if __name__ == '__main__':
    get_args()
